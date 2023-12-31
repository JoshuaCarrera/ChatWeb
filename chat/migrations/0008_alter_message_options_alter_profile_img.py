# Generated by Django 4.2.2 on 2023-07-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_file_alter_message_sender_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date_sent',)},
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='chat/profile_pics/default_profile_logo', upload_to='chat/profile_pics/'),
        ),
    ]
