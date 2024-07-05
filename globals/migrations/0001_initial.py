# Generated by Django 5.0.6 on 2024-07-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_text', models.CharField(max_length=100)),
                ('github_link', models.URLField()),
                ('blog_write_side_link', models.URLField()),
                ('project_side_url', models.URLField(blank=True)),
                ('blog_side_url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
