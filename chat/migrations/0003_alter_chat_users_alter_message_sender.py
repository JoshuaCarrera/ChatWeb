# Generated by Django 4.2.2 on 2023-06-28 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_from_user_message_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(related_name='chats', to='chat.profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sent', to='chat.profile'),
        ),
    ]
