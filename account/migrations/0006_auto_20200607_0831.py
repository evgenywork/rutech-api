# Generated by Django 2.2.13 on 2020-06-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test1591507905.843277@test.de', max_length=150, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(default=None, null=True, to='tag.Tag'),
        ),
    ]
