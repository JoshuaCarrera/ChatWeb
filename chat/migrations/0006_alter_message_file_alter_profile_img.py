# Generated by Django 4.2.2 on 2023-06-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, default=None, upload_to='chat_files'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default=None, upload_to='profile_pics'),
        ),
    ]
