# Generated by Django 5.1.3 on 2024-11-17 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport_News', '0009_alter_comment_published_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='Category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sport_News.category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sport_News.category'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sport_News.category'),
        ),
    ]
