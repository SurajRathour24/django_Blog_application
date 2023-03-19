# Generated by Django 4.1.4 on 2022-12-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Uncategorized', 'Uncategorized'), ('Travel', 'Travel'), ('Food', 'Food'), ('Tech', 'Tech'), ('Jobs', 'Jobs'), ('business', 'business'), ('sports', 'sports'), ('Trending', 'Trending'), ('Popular', 'Popular'), ('Inspiration', 'Inspiration')], default='Uncategorized', max_length=50),
        ),
    ]