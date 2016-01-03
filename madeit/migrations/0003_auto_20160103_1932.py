# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madeit', '0002_thread_thread_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='thread',
            name='thread_text',
            field=models.TextField(max_length=1000),
        ),
    ]
