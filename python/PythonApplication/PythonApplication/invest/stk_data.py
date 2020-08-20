import datetime
from quotool import his_quo
from tushare import get_realtime_quotes, get_index
from common import get_last_dvd_info


def ma(symbol, freq='D', ma_num=10):
    """
    ma
    :param symbol:
    :param freq:
    :param ma_num:
    :return:
    """
    if freq != 'D':
        print("Only support dayline")
        return None

    day_line_bars = day_bars(symbol, num=ma_num, qfq=True)

    closes = [bar['close'] for bar in day_line_bars]

    ma_value = sum(closes) / len(closes)

    return ma_value


def pre_ma(symbol, freq='D', ma_num=10, pre_days=1):
    """
    ma of sepcify previous days
    :param symbol:
    :param ma_num:
    :param pre_days:
    :param freq
    :return:
    """
    if freq != 'D':
        print("Only support dayline")
        return None

    day_line_bars = day_bars(symbol, num=ma_num + pre_days, qfq=True)

    closes = [bar['close'] for bar in day_line_bars]

    pre_closes = closes[pre_days - 1:pre_days - 1 + ma_num]

    ma_value = sum(pre_closes) / len(pre_closes)

    return ma_value


def day_bars(symbol, num=180, qfq=True, is_index=False):
    """
    day bar
    """
    day_line_bars = his_quo(symbol, num=num, is_index=is_index)
    first_his_date = str(day_line_bars[0]['date'])

    if not is_index:
        vol_zoom_mul = 100
        quo = get_realtime_quotes(symbol)
        last_date = quo.date.iloc[0]
    else:
        vol_zoom_mul = 1
        all_index_quo = get_index()
        quo = all_index_quo[all_index_quo.code == symbol]
        last_volume = int(quo.volume.iloc[0])
        first_his_volume = int(day_line_bars[0]['volume'])
        now = datetime.datetime.now()

        if abs(last_volume - first_his_volume) > 10:
            last_date = str(now.date())
        else:
            last_date = first_his_date

    if first_his_date < last_date:
        day_line_bars.insert(
            0,
            {
                'date': last_date, 
                'open': float(quo.open.iloc[0]),
                'high': float(quo.high.iloc[0]),
                'low': float(quo.low.iloc[0]),
                'close': float(quo['close' if is_index else 'price'].iloc[0]),
                'volume': float(quo.volume.iloc[0]) / vol_zoom_mul,
            }
        )
    
    if is_index:
        return day_line_bars[:num]

    if not qfq:
        return day_line_bars[:num]

    last_dvd_info = get_last_dvd_info(symbol)

    if not last_dvd_info:
        return day_line_bars[:num]

    date_dividend = last_dvd_info['divid_pay_date']
    cash_dividend = last_dvd_info['divid_cash_ps_before_tax']
    stock_dividend = last_dvd_info['divid_reserve_to_stock_ps'] or last_dvd_info['divid_stocks_ps']

    for day_bar in day_line_bars:
        if not day_bar['date'] < date_dividend:
            continue
        day_bar['open'] = round((day_bar['open'] - cash_dividend) / (1 + stock_dividend), 2)
        day_bar['high'] = round((day_bar['high'] - cash_dividend) / (1 + stock_dividend), 2)
        day_bar['low'] = round((day_bar['low'] - cash_dividend) / (1 + stock_dividend), 2)
        day_bar['close'] = round((day_bar['close'] - cash_dividend) / (1 + stock_dividend), 2)

    return day_line_bars[:num]


if __name__ == '__main__':
    rls = day_bars('603707', qfq=True)
    pass
