# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_seller_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referred_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
