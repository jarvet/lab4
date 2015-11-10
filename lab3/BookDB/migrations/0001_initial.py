# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Country', models.CharField(max_length=200, null=True)),
            ],
            options={
                'ordering': ['Name', 'Age', 'Country'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.IntegerField(serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=500, null=True)),
                ('Publisher', models.CharField(max_length=500, null=True)),
                ('PublishDate', models.DateField()),
                ('Price', models.CharField(max_length=100, null=True)),
                ('AuthorID', models.ForeignKey(related_name='authors', to='BookDB.Author')),
            ],
            options={
                'ordering': ['Title'],
            },
        ),
    ]
