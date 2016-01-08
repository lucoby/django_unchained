# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('madeit', '0003_auto_20160103_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 21, 58, 48, 15612, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
