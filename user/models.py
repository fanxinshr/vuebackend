from django.db import models
from rest_framework import serializers


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,unique=True,verbose_name="用户名")
    password = models.CharField(max_length=20,null=True,verbose_name="密码")
    remark = models.CharField(max_length=500,null=True,verbose_name="备注")
    class Meta:
        db_table = "sysUser"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

