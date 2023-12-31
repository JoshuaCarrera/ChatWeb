# Generated by Django 4.2.2 on 2023-06-28 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='from_user',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='message',
            name='to_user',
        ),
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(null=True, upload_to='chat_files'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('users', models.ManyToManyField(related_name='chats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chat'),
        ),
    ]
