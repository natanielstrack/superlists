# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160821_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_list',
            new_name='list',
        ),
    ]
