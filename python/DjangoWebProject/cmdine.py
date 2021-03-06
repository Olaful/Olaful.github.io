from subprocess import Popen
import os

# 开启轻量级服务
start_server = 'python manage.py runserver 0.0.0.0:1025'
# 创建应用
create_app = 'python manage.py startapp news'
# 创建数据库 默认sqlite3数据库,之后应用的更新就可以同步到
# 各自的数据库，如果有待提交的sql数据(通过django_migrations 
# 表检查)，则是提交数据至数据库,默认初始化会话表,管理员表,
# 用户认证表
create_or_up__appdata = 'python manage.py migrate'
# 移除app数据模型
rm_appdata = 'python manage.py migrate news zero'
# 创建数据库超级用户
create_superuser = 'python manage.py createsuperuser'
# 生成模型数据的迁移sql，在应用目录的 migrations目录下面
# 会生成更新信息
gener_sql = 'python manage.py makemigrations news'
# 查看某个应用数据迁移至数据库的sql，具体sql表现形式取决于你
# 配置的数据库类型
see_sql = 'python manage.py sqlmigrate news 0001'
# 打开shell,shell常用于调试项目
shell = 'python manage.py shell'
# 检查项目
check = 'python manage.py check'
# 填充脚本, 填充数据库数据
populate = 'python populate.py'

# 测试，使用news下面的tests.py文件中的
# 测试类来测试
test = 'python manage.py test news'

# 测试覆盖度
coverage = 'coverage run --source="." manage.py test news'

# 查看覆盖度数据,视图测试，模型测试覆盖率等
coverage_report = 'coverage report'

# 清理会话数据库,由于随着连接用户的增加，数据库会越来越大
clear_session_data = 'python manage.py clearsessions'


# shell中的命令
# 查看所有表
# Category.objects.all()
# 创建实例
# c = Category(title='hello')
# c.save()
# 查看数据
# c.title

if __name__ == '__main__':
    os.chdir(r'DjangoWebProject/django_newswebsite')
    Popen(start_server, stdout = None, stderr = None, shell=True)