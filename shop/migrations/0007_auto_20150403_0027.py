# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_saleitem_dummyfacebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='title',
            field=models.CharField(max_length=b'60'),
            preserve_default=True,
        ),
    ]
