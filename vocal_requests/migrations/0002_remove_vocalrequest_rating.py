# Generated by Django 4.2.7 on 2023-11-24 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocal_requests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocalrequest',
            name='rating',
        ),
    ]
