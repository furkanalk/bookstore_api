# Generated by Django 4.1.7 on 2023-08-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_user_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]