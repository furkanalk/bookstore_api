# Generated by Django 4.1.7 on 2023-08-03 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_rename_username_user_name_user_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
    ]
