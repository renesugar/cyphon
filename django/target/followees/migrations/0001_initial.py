# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('name', 'Name'), ('username', 'Username')], max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='followees.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Followee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LegalName',
            fields=[
                ('followee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='followees.Followee')),
                ('first', models.CharField(max_length=255)),
                ('middle', models.CharField(default='', max_length=255)),
                ('last', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='followee',
            name='associates',
            field=models.ManyToManyField(blank=True, related_name='_followee_associates_+', to='followees.Followee'),
        ),
        migrations.AddField(
            model_name='account',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='followees.Followee'),
        ),
    ]
