# Generated by Django 3.2.6 on 2021-09-01 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fauxblog', '0004_alter_imagepost_posted_by'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
