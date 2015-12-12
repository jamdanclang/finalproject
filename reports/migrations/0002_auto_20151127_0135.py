# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('building', models.ForeignKey(to='reports.Building')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='building',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
