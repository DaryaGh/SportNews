# Generated by Django 5.1.3 on 2024-12-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport_News', '0019_remove_news_image_remove_news_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Sliders')),
                ('title', models.CharField(default=None, max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
