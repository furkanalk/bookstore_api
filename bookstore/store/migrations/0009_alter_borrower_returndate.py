# Generated by Django 4.1.7 on 2023-08-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_borrower_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='returndate',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
