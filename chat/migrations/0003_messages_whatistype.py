# Generated by Django 4.1.4 on 2023-07-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_first_user_room_second_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='WhatisType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]