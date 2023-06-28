# Generated by Django 4.2.2 on 2023-06-27 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to=None)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]