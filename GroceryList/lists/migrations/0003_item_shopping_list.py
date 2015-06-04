# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_shoppinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shopping_list',
            field=models.ForeignKey(default=1, to='lists.ShoppingList'),
            preserve_default=False,
        ),
    ]
