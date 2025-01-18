# Generated by Django 5.1.3 on 2024-11-17 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport_News', '0010_alter_media_category_alter_news_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='createdUsers',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_0', to='Sport_News.user'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updatedUsers',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_1', to='Sport_News.user'),
        ),
    ]
