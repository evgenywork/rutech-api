# Generated by Django 2.2.13 on 2020-06-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='background_name',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]
