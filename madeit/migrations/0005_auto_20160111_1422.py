# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madeit', '0004_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='guest', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='user',
            field=models.CharField(default='guest', max_length=32),
            preserve_default=False,
        ),
    ]
