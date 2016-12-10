# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_info', '0003_auto_20161210_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mas_states',
            name='country',
            field=models.ForeignKey(default=2, to='Company_info.mas_countries'),
        ),
    ]
