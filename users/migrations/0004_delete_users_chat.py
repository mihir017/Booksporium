# Generated by Django 3.1.4 on 2021-04-05 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users_chat',
        ),
    ]