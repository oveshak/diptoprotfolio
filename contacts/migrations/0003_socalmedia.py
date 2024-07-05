# Generated by Django 5.0.6 on 2024-07-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactus_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socal_media_name', models.CharField(max_length=20)),
                ('socal_media_url', models.URLField()),
            ],
        ),
    ]