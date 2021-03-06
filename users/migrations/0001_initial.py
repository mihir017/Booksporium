# Generated by Django 3.1.4 on 2021-04-05 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20210402_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to='accounts.users')),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_user', to='accounts.users')),
            ],
        ),
    ]
