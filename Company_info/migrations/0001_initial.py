# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mas_company_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=30)),
                ('company_caption', models.CharField(max_length=100, null=True, blank=True)),
                ('company_reg_info', models.CharField(max_length=30, null=True, blank=True)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50, null=True, blank=True)),
                ('address3', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=10)),
                ('phone1', models.CharField(max_length=10)),
                ('phone2', models.CharField(max_length=10, null=True, blank=True)),
                ('website', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('postcode', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='mas_states',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mas_company_profile',
            name='State',
            field=models.ForeignKey(to='Company_info.mas_states'),
        ),
    ]
