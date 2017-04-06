# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-04 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0010_populate_previous_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissionattributes',
            name='previous_submission',
            field=models.OneToOneField(blank=True, help_text='A reference to the most recent submission for this CGAC within the same fiscal year', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='submissions.SubmissionAttributes'),
        ),
    ]