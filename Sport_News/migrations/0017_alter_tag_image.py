# Generated by Django 5.1.3 on 2024-11-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport_News', '0016_rename_description_contactus_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ManyToManyField(related_name='images_tag', to='Sport_News.image'),
        ),
    ]
