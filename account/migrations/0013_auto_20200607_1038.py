# Generated by Django 2.2.13 on 2020-06-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200607_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test1591515514.1327183@test.de', max_length=150, unique=True, verbose_name='Email'),
        ),
    ]