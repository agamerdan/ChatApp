# Generated by Django 4.1.4 on 2023-07-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resim',
            field=models.FileField(default='media/avatar.png', null=True, upload_to=''),
        ),
    ]
