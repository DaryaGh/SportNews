# Generated by Django 5.1.3 on 2024-11-17 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport_News', '0006_replyanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replyanswer',
            name='avatar',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sport_News.avatar'),
        ),
    ]
