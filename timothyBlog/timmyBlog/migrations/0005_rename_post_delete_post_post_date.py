# Generated by Django 3.2.5 on 2021-07-24 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timmyBlog', '0004_post_post_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_delete',
            new_name='post_date',
        ),
    ]