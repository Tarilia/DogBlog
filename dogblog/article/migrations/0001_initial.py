# Generated by Django 4.2.7 on 2024-05-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Heading')),
                ('content', models.TextField(blank=True, verbose_name='Article text')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Change time')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
