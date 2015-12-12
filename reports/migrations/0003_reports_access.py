# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20151127_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='access',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
