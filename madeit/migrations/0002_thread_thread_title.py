# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madeit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='thread_title',
            field=models.CharField(default='hello world', max_length=200),
            preserve_default=False,
        ),
    ]
