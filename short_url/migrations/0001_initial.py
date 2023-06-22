# Generated by Django 4.2.2 on 2023-06-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_access', models.DateTimeField(blank=True, null=True)),
                ('time_followed', models.PositiveIntegerField(default=0)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=7, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]