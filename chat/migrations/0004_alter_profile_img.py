# Generated by Django 4.2.2 on 2023-06-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chat_users_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default=True, upload_to='profile_pics'),
        ),
    ]
