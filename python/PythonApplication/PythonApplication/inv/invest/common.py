import sqlite3
import datetime
import re
import pandas as pd
from baostock import query_dividend_data
from baostock import login as bao_stk_login
from invest import util

_DB_SQLITE = {}
_DB_FILE = 'sqlite.db'
_POS = []
_MARKET_TIME = []


def init_data():
    _load_pos()
    _init_market_time()


def _get_sqllite(name="test"):
    if _DB_SQLITE.get(name, None):
        return _DB_SQLITE[name]

    class SQLite:
        def __init__(self):
            self.conn = sqlite3.connect(_DB_FILE)
            self.cursor = self.conn.cursor()
            self.sql_result = ()

        def execute(self, sql):
            is_insert_sql = sql.strip().lower().startswith('select') | \
                            sql.strip().lower().startswith('replace')

            begin = "BEGIN IMMEDIATE"
            commit = "COMMIT"

            if is_insert_sql:
                try:
                    self.cursor.execute(begin)
                except sqlite3.OperationalError as e:
                    print(f"sqlite exe error => sql: {begin}, msg: {str(e)}")

            self.cursor.execute(sql)
            self.sql_result = self.cursor.fetchall()

            if is_insert_sql:
                self.cursor.execute(commit)

        def fetchone(self):
            if len(self.sql_result) > 0:
                return self.sql_result[0]
            return ()

        def fetchall(self):
            rls = self.sql_result
            return rls

    db_instance = SQLite()

    _DB_SQLITE[name] = db_instance

    return db_instance


def _load_pos():
    db = util.get_mysql('test')
    query_sql = "SELECT * FROM `position` " \
                " WHERE `is_valid` = 1"
    db.execute(query_sql)
    global _POS
    _POS = db.fetchall()


def _init_market_time():
    open_time = util.get_config('market', 'open_time')
    open_time_split = open_time.split(':')
    hour = int(open_time_split[0])
    minute = int(open_time_split[1])

    open_time_ts = datetime.datetime.today().replace(hour=hour, minute=minute).timestamp()

    close_time = util.get_config('market', 'close_time')
    close_time_split = close_time.split(':')
    hour = int(close_time_split[0])
    minute = int(close_time_split[1])

    close_time_ts = datetime.datetime.today().replace(hour=hour, minute=minute).timestamp()

    _MARKET_TIME.extend([open_time_ts, close_time_ts])


def get_openclose_time():
    return _MARKET_TIME


def get_all_pos():
    return _POS


def get_last_dvd_info(symbol):
    db = _get_sqllite('dvd_db')

    def check_table():
        try:
            exist_sql = 'SELECT 1 FROM `tb_dvd`'
            db.execute(exist_sql)
        except:
            create_table_sql = """CREATE TABLE `tb_dvd` (
                `code` char(32) NOT NULL, -- '标的'
                `dividOperateDate` date default NULL, -- '除权除息日期'
                `dividPayDate` date default NULL, -- '	派息日'
                `dividCashPsBeforeTax` float default '0.0', -- '每股股利税前',
                `dividCashPsAfterTax` float default '0.0', -- '每股股利税后'
                `dividStocksPs` float default '0.0', -- '每股红股'
                `dividReserveToStockPs` float default '0.0', -- '每股转增资本'
                `dividCashStock` TEXT, -- '分红送转(每股派息数(税前)+每股送股数+每股转增股本数)'
                `updatetime` datetime NOT NULL, -- '更新时间'
                PRIMARY KEY (`code`, `dividOperateDate`)
            )"""
            db.execute(create_table_sql)
    check_table()

    query_sql = f"SELECT `dividPayDate`, `dividCashPsBeforeTax`, \
     `dividStocksPs`, `dividReserveToStockPs`, `updatetime` FROM `tb_dvd` WHERE \
        `code` = '{symbol}' ORDER BY `dividPayDate` DESC LIMIT 1"
    db.execute(query_sql)
    dvd_info = db.fetchone()
    re_fetch = False

    if not dvd_info:
        re_fetch = True
    else:
        update_date = datetime.datetime.strptime(dvd_info[-1][:10], '%Y-%m-%d').date()
        today = datetime.datetime.today().date()   
        if update_date != today:
            re_fetch = True

    if not re_fetch:
        divid_pay_date = dvd_info[0]
        if not divid_pay_date:
            return {}
        return {
            'divid_pay_date': divid_pay_date,
            'divid_cash_ps_before_tax': dvd_info[1],
            'divid_stocks_ps': dvd_info[2],
            'divid_reserve_to_stock_ps': dvd_info[3]
        }

    bao_stk_login()

    def to_db(rs_list, fields):
        insert_sql = """REPLACE INTO `tb_dvd`(
            `code`, `dividOperateDate`, `dividPayDate`, `dividCashPsBeforeTax`,
            `dividCashPsAfterTax`, `dividStocksPs`, `dividReserveToStockPs`,`dividCashStock`,
            `updatetime`
        ) VALUES(
            '{code}', '{dividOperateDate}', '{dividPayDate}', {dividCashPsBeforeTax},
            {dividCashPsAfterTax}, {dividStocksPs}, {dividReserveToStockPs}, '{dividCashStock}',
            '{updatetime}'
        )"""
        insert_param = {
            'code': symbol, 'dividOperateDate': None, 'dividPayDate': None, 'dividCashPsBeforeTax': 0.0,
            'dividCashPsAfterTax': 0.0, 'dividStocksPs': 0.0, 'dividReserveToStockPs': 0.0, 'dividCashStock': '',
            'updatetime': str(today)
        }

        if not rs_list:
            db.execute(insert_sql.format(**insert_param))
            return
    
        result_dividend = pd.DataFrame(rs_list, columns=fields)

        for _, row in result_dividend.iterrows():
            dividCashPsAfterTax = row.dividCashPsAfterTax
            rls = re.search('[\u4e00-\u9fa5]', dividCashPsAfterTax)
            if rls:
                start = rls.start()
                dividCashPsAfterTax = float(dividCashPsAfterTax[:start])
            else:
                if isinstance(dividCashPsAfterTax, str):
                    print("dividCashPsAfterTax is str")
                    dividCashPsAfterTax = 0.0
                else:
                    dividCashPsAfterTax = float(dividCashPsAfterTax)

            insert_param.update({
                'dividOperateDate': row.dividOperateDate,
                'dividPayDate': row.dividPayDate,
                'dividCashPsBeforeTax': row.dividCashPsBeforeTax if row.dividCashPsBeforeTax else 0,
                'dividCashPsAfterTax': dividCashPsAfterTax,
                'dividStocksPs': row.dividStocksPs if row.dividStocksPs else 0,
                'dividReserveToStockPs': row.dividReserveToStockPs if row.dividReserveToStockPs else 0,
                'dividCashStock': row.dividCashStock,
            })

            db.execute(insert_sql.format(**insert_param))

    today = datetime.datetime.today()
    pre_year_today = today - datetime.timedelta(days=366)
    today_year = today.year
    pre_year = pre_year_today.year

    rs_list = []
    fields = []
    code = f"sh.{symbol}" if symbol.startswith('60') else f"sz.{symbol}"
    for year in [today_year, pre_year]:
        rs_dividend = query_dividend_data(code=code, year=year, yearType="report")

        while (rs_dividend.error_code == '0') & rs_dividend.next():
            rs_list.append(rs_dividend.get_row_data())

        if rs_list:
            fields = rs_dividend.fields

    to_db(rs_list, fields)

    db.execute(query_sql)
    dvd_info = db.fetchone()
    divid_pay_date = dvd_info[0]
    if not divid_pay_date:
        return {}
    return {
        'divid_pay_date': divid_pay_date,
        'divid_cash_ps_before_tax': dvd_info[1],
        'divid_stocks_ps': dvd_info[2],
        'divid_reserve_to_stock_ps': dvd_info[3]
    }


def get_stock_pool(pool_name):
    """
    get symbol list from pool
    :param pool_name:
    :return:
    """
    db = util.get_mysql("test")
    query_sql = "SELECT `code` FROM `code_pool` " \
                f" WHERE `pool` = '{pool_name}'"
    db.execute(query_sql)

    pool_info = db.fetchall()
    code_list = [code['code'] for code in pool_info]

    return code_list


def get_parallel_high_low_key_pos(day_bars, wind=30, inner_percent=0.01, outer_percent=0.02, turn_num=2):
    """
    get the key pos of parallel high and low
    :param day_bars:
    :param wind:
    :param inner_percent:
    :param outer_percent:
    :param turn_num:
    :return:
    """
    wind_bar_info = []
    for i in range(0, len(day_bars), wind):
        bar_info = {}
        bar_info['high'] = {}
        bar_info['low'] = {}

        wind_bars = day_bars[i:i+wind]

        max_bar = max(wind_bars, key=lambda bar: bar['high'])
        min_bar = min(wind_bars, key=lambda bar: bar['low'])

        bar_info['high']['bar'] = max_bar
        bar_info['low']['bar'] = min_bar

        max_price = max_bar['high']
        min_price = min_bar['low']

        high_side_bars = []
        low_side_bars = []
        
        for bar in wind_bars:
            high_change = max_price / bar['high'] - 1
            low_change = min_price / bar['low'] - 1

            if abs(high_change) <= inner_percent and bar != max_bar:
                high_side_bars.append(bar)
            
            if abs(low_change) <= inner_percent and bar != min_bar:
                low_side_bars.append(bar)
        
        bar_info['high']['side_bars'] = high_side_bars
        bar_info['low']['side_bars'] = low_side_bars

        wind_bar_info.append(bar_info)

    wind_bar_cat = {}
    for win_bar in wind_bar_info:
        high_cat = None
        low_cat = None
        high_cat_found = False
        low_cat_found = False

        for price in wind_bar_cat.keys():
            high_change = win_bar['high']['bar']['high'] / price - 1
            low_change = win_bar['low']['bar']['low'] / price - 1

            if not high_cat_found and abs(high_change) <= outer_percent:
                high_cat = price
                high_cat_found = True
            if not low_cat_found and abs(low_change) <= outer_percent:
                low_cat = price
                low_cat_found = True

        if high_cat:
            wind_bar_cat[high_cat].append(win_bar['high']['bar'])
            wind_bar_cat[high_cat].extend(win_bar['high']['side_bars'])
        else:
            wind_bar_cat[win_bar['high']['bar']['high']] = [win_bar['high']['bar']]
            wind_bar_cat[win_bar['high']['bar']['high']].extend(win_bar['high']['side_bars'])

        if low_cat:
            wind_bar_cat[low_cat].append(win_bar['low']['bar'])
            wind_bar_cat[low_cat].extend(win_bar['low']['side_bars'])
        else:
            wind_bar_cat[win_bar['low']['bar']['low']] = [win_bar['low']['bar']]
            wind_bar_cat[win_bar['low']['bar']['low']].extend(win_bar['low']['side_bars'])

    key_pos = [price for price, bl in wind_bar_cat.items() if len(bl) >= turn_num]    
    key_pos.sort(reverse=False)

    return key_pos


def get_gap_key_pos(day_bars, threshold):
    """
    get key poss of gap
    :param day_bars:
    :param threshold:
    :return:
    """
    key_poss = []

    for i in range(len(day_bars) - 1):
        cur_bar = day_bars[i]
        next_bar = day_bars[i+1]

        cur_min_oc = min(cur_bar['open'], cur_bar['close'])
        next_max_oc = max(next_bar['open'], next_bar['close'])
        if cur_min_oc > next_max_oc:
            up_gap_change = cur_min_oc / next_max_oc - 1
            if up_gap_change >= threshold:
                key_poss.append(cur_min_oc)

        cur_max_oc = max(cur_bar['open'], cur_bar['close'])
        next_min_oc = min(next_bar['open'], next_bar['close'])
        if next_min_oc > cur_max_oc:
            down_gap_change = next_min_oc / cur_max_oc - 1
            if down_gap_change >= threshold:
                key_poss.append(cur_max_oc)

    key_poss.sort(reverse=False)

    return key_poss


def get_ma_list(bars, freq=5, num=10):
    """
    get ma list
    """
    closes = [bar['close'] for bar in bars]
    ma_list = []

    for i in range(0, num):
        freq_closes = closes[i:i+freq]
        ma = round(sum(freq_closes) / len(freq_closes), 3)
        ma_list.append(ma)

    return ma_list


def merge_bars(bars):
    """
    merge bars to a bar
    """
    if not bars:
        return None

    if len(bars) < 2:
        return bars[0]

    o = bars[-1]['open']
    h = max(bars, key=lambda bar: bar['high'])['high']
    l = min(bars, key=lambda bar: bar['low'])['low']
    c = bars[0]['close']
    v = sum(bar['volume'] for bar in bars)

    merge_bar = {
        'date': bars[0]['date'],
        'open': o,
        'high': h,
        'low': l,
        'close': c,
        'volume': v
    }

    return merge_bar


def is_cross_star(day_bar, open_close_change=0.0025, high_low_change=0.025):
    """
    if it is a cross star
    """
    openclose_change = day_bar['open'] / day_bar['close'] - 1
    if abs(openclose_change) > open_close_change:
        return False

    if day_bar['high'] == max(day_bar['close'], day_bar['open']):
        return False

    if day_bar['low'] == min(day_bar['close'], day_bar['open']):
        return False

    highlow_change = day_bar['high'] / day_bar['low'] - 1
    if highlow_change >= high_low_change:
        return True

    return False


def is_hang_line(day_bar, mul=1, up_percent=0.009):
    """
    if it is a hang line
    """
    if day_bar['close'] == day_bar['open']:
        return False

    upper_shadow_change = day_bar['high'] / max(day_bar['close'], day_bar['open']) - 1
    if upper_shadow_change > up_percent:
        return False

    lower_shadow_diff = min(day_bar['close'], day_bar['open']) - day_bar['low']
    if lower_shadow_diff == 0:
        return False

    entity_part_diff = abs(day_bar['close'] - day_bar['open'])
    
    mul_diff = lower_shadow_diff / entity_part_diff
    if mul_diff >= mul:
        return True

    return False


def is_meteor_line(day_bar, mul=1, down_percent=0.009):
    """
    if it is a meteor line
    """
    if day_bar['close'] == day_bar['open']:
        return False

    lower_shadow_change = min(day_bar['close'], day_bar['open']) / day_bar['low'] - 1
    if lower_shadow_change > down_percent:
        return False

    upper_shadow_diff = day_bar['high'] - max(day_bar['close'], day_bar['open'])
    if upper_shadow_diff == 0:
        return False

    entity_part_diff = abs(day_bar['close'] - day_bar['open'])
    
    mul_diff = upper_shadow_diff / entity_part_diff
    if mul_diff >= mul:
        return True

    return False


def is_T_line(day_bar, open_close_change=0.0025, high_low_change=0.025, up_percent=0.009):
    """
    if it is a cross star
    """
    openclose_change = day_bar['open'] / day_bar['close'] - 1
    if abs(openclose_change) > open_close_change:
        return False

    upper_shadow_change = day_bar['high'] / max(day_bar['close'], day_bar['open']) - 1
    if upper_shadow_change > up_percent:
        return False

    highlow_change = day_bar['high'] / day_bar['low'] - 1
    if highlow_change >= high_low_change:
        return True

    return False


def is_bullish_swallow(bars, percent=0.002):
    """
    if it is a bullish swallow
    """
    if len(bars) < 2:
        return False

    last_day_bar = bars[0]
    if last_day_bar['close'] < last_day_bar['open']:
        return False

    pre_day_bar = bars[1]
    if pre_day_bar['close'] > pre_day_bar['open']:
        return False

    upper_change = last_day_bar['close'] / pre_day_bar['open'] - 1
    if upper_change < 0:
        if abs(upper_change) > percent:
            return False

    lower_change = last_day_bar['open'] / pre_day_bar['close'] - 1
    if lower_change > 0:
        if abs(lower_change) > percent:
            return False

    return True


def is_pierce_line(bars, percent=0.009):
    """
    if it is a bullish swallow
    """
    if len(bars) < 2:
        return False

    last_day_bar = bars[0]
    if last_day_bar['close'] < last_day_bar['open']:
        return False

    pre_day_bar = bars[1]
    if pre_day_bar['close'] > pre_day_bar['open']:
        return False

    lower_change = last_day_bar['open'] / pre_day_bar['close'] - 1
    if lower_change > 0:
        if abs(lower_change) > percent:
            return False

    if last_day_bar['close'] > pre_day_bar['open']:
        return False
    
    pre_day_bar_mid_price = (pre_day_bar['open'] + pre_day_bar['close']) / 2

    if last_day_bar['close'] < pre_day_bar_mid_price:
        return False

    return True


def is_start_morrow_star(bars, percent=0.002, open_close_change=0.0025):
    """
    if it is a start morrow star
    """
    if len(bars) < 3:
        return False

    last_day_bar = bars[0]

    if last_day_bar['close'] < last_day_bar['open']:
        return False

    pre_day_bar = bars[1]

    if not is_cross_star(pre_day_bar, open_close_change):
        return False

    pre_pre_day_bar = bars[2]
    if pre_pre_day_bar['close'] > pre_pre_day_bar['open']:
        return False

    lower_change = last_day_bar['open'] / pre_pre_day_bar['close'] - 1
    if lower_change > 0:
        if abs(lower_change) > percent:
            return False

    pre_pre_day_bar_mid_price = (pre_pre_day_bar['open'] + pre_pre_day_bar['close']) / 2

    if last_day_bar['close'] < pre_pre_day_bar_mid_price:
        return False

    return True


def is_go_ahead_red_three_soldier(day_bars):
    """
    if it is a red three soldier that go ahead
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change < 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change < 0:
        return False

    if first_day_change < pre_day_change:
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change < 0:
        return False

    if pre_day_change > pre_pre_day_change:
        return True

    return False


def is_stagnant_red_three_soldier(day_bars):
    """
    if it is a stagnant red three soldier
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change < 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change < 0:
        return False

    if first_day_change > pre_day_change:
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change < 0:
        return False

    if pre_day_change < pre_pre_day_change:
        return True

    return False


def is_stagnant_rise_red_three_soldier(day_bars):
    """
    if it is a stagnant rise red three soldier
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change < 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change < 0:
        return False

    if first_day_change > pre_day_change:
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change < 0:
        return False

    if pre_day_change > pre_pre_day_change:
        return True

    return False
    
    
def is_go_ahead_black_three_soldier(day_bars):
    """
    if it is a black three soldier that go ahead
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change >= 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change >= 0:
        return False

    if abs(first_day_change) < abs(pre_day_change):
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change >= 0:
        return False

    if abs(pre_day_change) > abs(pre_pre_day_change):
        return True

    return False


def is_stagnant_black_three_soldier(day_bars):
    """
    if it is a stagnant black three soldier
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change >= 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change >= 0:
        return False

    if abs(first_day_change) > abs(pre_day_change):
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change >= 0:
        return False

    if abs(pre_day_change) < abs(pre_pre_day_change):
        return True

    return False


def is_stagnant_down_black_three_soldier(day_bars):
    """
    if it is a stagnant down black three soldier
    """
    if len(day_bars) < 3:
        return False

    first_day_bar = day_bars[0]
    first_day_change = first_day_bar['close'] / first_day_bar['open'] - 1
    if first_day_change >= 0:
        return False

    pre_day_bar = day_bars[1]
    pre_day_change = pre_day_bar['close'] / pre_day_bar['open'] - 1
    if pre_day_change >= 0:
        return False

    if abs(first_day_change) > abs(pre_day_change):
        return False

    pre_pre_day_bar = day_bars[2]
    pre_pre_day_change = pre_pre_day_bar['close'] / pre_pre_day_bar['open'] - 1
    if pre_pre_day_change >= 0:
        return False

    if abs(pre_day_change) > abs(pre_pre_day_change):
        return True

    return False


def is_in_key_pos(bar, key_pos: list = None, change=0.001):
    """
    if in the key position
    """
    high = bar['high'] * (1 + change)
    low = bar['low'] * (1 + change)

    for pos in key_pos:
        if low <= pos <= high:
            return True
    
    return False


def is_in_high_or_low_pos(closes, days=2, direction='down'):
    """
    if in high or low position
    """
    decline_or_gain_days = util.continuous_decline_or_gain(closes, direction)

    if decline_or_gain_days >= days:
        return True

    return False


def is_noticeable_bar(bar, change=0.06):
    """
    if it is a noticeable bar
    """
    hig_low_change = bar['high'] / bar['low'] - 1

    if hig_low_change >= change:
        return True

    return False


def is_pretend_breakthrough_key_pos(bar, key_pos, change=0.009):
    """
    if pretend to breakthrough the key position
    """
    if bar['close'] < key_pos:
        return False

    key_low_change = key_pos  / bar['low'] - 1

    if key_low_change >= change:
        return True

    return False


def is_left_swallow_right_bar(day_bars):
    """
    if left bar swallow right bar
    """
    if len(day_bars) < 2:
        return False

    last_day_bar = day_bars[0]
    pre_day_bar = day_bars[1]

    if pre_day_bar['high'] >= max(last_day_bar['open'], last_day_bar['close']) \
     and pre_day_bar['low'] <= min(last_day_bar['open'], last_day_bar['close']):
        return True

    return False


def is_last_change_gt_pre_bar(day_bars):
    """
    if change of last bar greater than previous
    """
    if len(day_bars) < 2:
        return False

    last_day_bar = day_bars[0]
    pre_day_bar = day_bars[1]

    last_bar_change = last_day_bar['high'] / last_day_bar['low'] - 1
    pre_bar_change = pre_day_bar['high'] / pre_day_bar['low'] - 1

    if last_bar_change > pre_bar_change:
        return True

    return False


def is_key_pos_pl_gt_specify_value(price, key_pos: list = None, pl=1.5, change=0.01):
    """
    if the profit-loss ratio gt specify value
    """
    upper_key_pos = [pos for pos in key_pos if pos > price]
    if not upper_key_pos:
        return False

    nearby_upper_key_pos = min(upper_key_pos)

    lower_key_pos = [pos for pos in key_pos if pos < price]
    if not lower_key_pos:
        return False

    nearby_lower_key_pos = max(lower_key_pos)

    upper_profit = nearby_upper_key_pos * (1 + change) - price
    lower_loss = price - nearby_lower_key_pos * (1 - change)

    pl_ratio = upper_profit / lower_loss

    if pl_ratio >= pl:
        return True

    return False
    