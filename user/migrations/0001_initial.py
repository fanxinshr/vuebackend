# Generated by Django 4.2.17 on 2025-01-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('remark', models.CharField(max_length=500, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'sysUser',
            },
        ),
    ]
