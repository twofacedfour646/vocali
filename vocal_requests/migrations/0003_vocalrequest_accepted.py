# Generated by Django 4.2.7 on 2023-12-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocal_requests', '0002_remove_vocalrequest_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocalrequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]