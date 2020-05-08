# Generated by Django 2.2.6 on 2020-04-20 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_users_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo_id',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='photo_id',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='image_id',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
