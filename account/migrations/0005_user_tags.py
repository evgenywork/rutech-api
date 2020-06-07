# Generated by Django 2.2.13 on 2020-06-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_remove_tag_users'),
        ('account', '0004_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]
