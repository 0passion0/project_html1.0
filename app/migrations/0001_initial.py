# Generated by Django 4.1.5 on 2023-03-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userment',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('gender', models.CharField(max_length=5, verbose_name='性别')),
                ('math', models.IntegerField(verbose_name='数学')),
                ('python', models.IntegerField(verbose_name='python')),
                ('C', models.IntegerField(verbose_name='C')),
                ('coun', models.IntegerField(verbose_name='总分')),
            ],
        ),
    ]
