# Generated by Django 4.1.4 on 2022-12-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_post_author_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='featured_image/%Y/%m/%d/'),
        ),
    ]
