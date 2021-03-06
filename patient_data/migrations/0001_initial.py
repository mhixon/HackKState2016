# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encounter_id', models.IntegerField(default=0)),
                ('patient_nbr', models.IntegerField(default=0)),
                ('race', models.IntegerField(default=0)),
                ('gender', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('admission_type_id', models.CharField(max_length=200)),
                ('discharge_disposition_id', models.CharField(max_length=200)),
                ('admission_source_id', models.CharField(max_length=200)),
                ('time_in_hospital', models.CharField(max_length=200)),
                ('payer_code', models.CharField(max_length=200)),
                ('medical_specialty', models.CharField(max_length=200)),
                ('num_lab_procedures', models.CharField(max_length=200)),
                ('num_procedures', models.CharField(max_length=200)),
                ('num_medications', models.CharField(max_length=200)),
                ('number_outpatient', models.CharField(max_length=200)),
                ('number_emergency', models.CharField(max_length=200)),
                ('number_inpatient', models.CharField(max_length=200)),
                ('diag_1', models.CharField(max_length=200)),
                ('diag_2', models.CharField(max_length=200)),
                ('diag_3', models.CharField(max_length=200)),
                ('num_diagnoses', models.CharField(max_length=200)),
                ('max_glu_serum', models.CharField(max_length=200)),
                ('A1Cresult', models.CharField(max_length=200)),
                ('med_feature', models.CharField(max_length=200)),
                ('change', models.CharField(max_length=200)),
                ('diabetesMed', models.CharField(max_length=200)),
                ('readmitted', models.CharField(max_length=200)),
            ],
        ),
    ]
