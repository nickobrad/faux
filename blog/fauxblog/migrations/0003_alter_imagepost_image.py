# Generated by Django 3.2.6 on 2021-09-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauxblog', '0002_auto_20210901_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
