from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     pass
    # nick_name = models.CharField(max_length=25, verbose_name='昵称')
    # email = models.EmailField(max_length=255, verbose_name='邮箱')
    # user_address = models.CharField(max_length=35, verbose_name='住址')


# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['nick_name', 'user_address', 'email', 'my_order']
#
#     # 自定义admin后台显示字段
#     def my_order(self, obj):
#         return obj.Order.order_no
#
#     my_order.short_description = "用户"
