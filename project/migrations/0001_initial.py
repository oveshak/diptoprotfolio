# Generated by Django 5.0.6 on 2024-07-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('date', models.DateField()),
                ('language', models.CharField(max_length=100)),
                ('project_url', models.TextField(max_length=50)),
                ('project_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('project_item', models.ManyToManyField(to='project.projectitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]