# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_info', '0002_auto_20161210_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='mas_countries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mas_states',
            name='country',
            field=models.ForeignKey(default=1, to='Company_info.mas_countries'),
            preserve_default=False,
        ),
    ]
