from django.db import models
from django.utils import timezone
#from django.template.defaultfilters import slugify
from uuslug import slugify
from django.contrib.auth.models import User

import datetime

# 一个类对应一个模型, 模型对应数据库中的表
# 数据库类型不需要关心，因为ORM会自动根据
# 数据库类型生成对应的sql语句
# 这就是ORM对象关系映射
# 分类类，
class Category(models.Model):
    MAX_NAME_LEN = 128

    # 自定义字段，默认有id字段，用作主键，可以自定义修改
    name = models.CharField(max_length=MAX_NAME_LEN, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    # 其它字段, 字段名被重命名第一个参数，如果提供的话
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    # 别名字段,标识每个模型实例
    slug = models.SlugField(unique=True)

    # 由于管理界面显示Categorys(默认),所以定义以下类进行更正
    # 元类，再次指定model类的配置，如表名称通过db_table
    # 指定，定义唯一主键等
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def is_outdate(self):
        return self.pub_date <= timezone.now() - datetime.timedelta(days=3)
    is_outdate.admin_order_field = 'pub_date'
    is_outdate.boolean = True
    # 字段显示名称
    is_outdate.short_description = 'outdate?'

    def save(self, *args, **kwargs):
        # slugify函数会把字符串中的空白符用'-'替换,大写变为小写
        self.slug = slugify(self.name)
        self.views = self.views
        super(Category, self).save(*args, **kwargs)

# 页面类
class Page(models.Model):
    # 一对多关系，还有OneToOneField一对一关系
    # ManyToManyField多对多关系
    # 会映射至Category的id字段，会自动创建索引
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(default=datetime.datetime.now())
    last_visit = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

# 用户模型扩展
class UserProfile(models.Model):
    # 建立与User模型之间的联系,User模型默认用username, password, email等属性
    # OneToOneField的话当前模型实例与User实例会同时被插入数据库
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 额外增加的用户属性
    website = models.URLField(blank=True)
    # profile_images文件夹会在media文件夹下建立
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
