# Generated by Django 4.1.3 on 2022-12-15 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_post_author_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_designation',
        ),
    ]
