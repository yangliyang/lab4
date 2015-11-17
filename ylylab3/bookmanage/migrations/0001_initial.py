# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=3)),
                ('Country', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=10)),
                ('Title', models.CharField(max_length=10)),
                ('AuthorID', models.CharField(max_length=10)),
                ('Publisher', models.CharField(max_length=20)),
                ('PublishDate', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
