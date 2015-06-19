# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=32)),
                ('access', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_name', models.CharField(max_length=32)),
                ('hex_stat', models.CharField(max_length=6)),
                ('access', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=100)),
                ('date_create', models.DateTimeField(null=True)),
                ('files', models.FileField(null=True, upload_to=b'files/')),
                ('id_category', models.ForeignKey(to='server_note.Category')),
                ('id_color', models.ForeignKey(to='server_note.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=32)),
                ('access', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('id_category', models.ManyToManyField(to='server_note.Category')),
                ('id_color', models.ManyToManyField(to='server_note.Color')),
                ('id_tag', models.ManyToManyField(to='server_note.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='id_tag',
            field=models.ManyToManyField(to='server_note.Tag'),
        ),
        migrations.AddField(
            model_name='note',
            name='id_user',
            field=models.ForeignKey(to='server_note.User'),
        ),
    ]
