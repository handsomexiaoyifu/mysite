# Generated by Django 2.0 on 2021-04-24 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_oauthrelationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oauthrelationship',
            name='user',
        ),
        migrations.DeleteModel(
            name='OAuthRelationship',
        ),
    ]
