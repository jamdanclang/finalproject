# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_reports_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='campus',
        ),
    ]
