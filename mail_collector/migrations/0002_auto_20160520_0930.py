# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_collector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='files',
            field=models.FileField(upload_to='', blank=True),
        ),
    ]
