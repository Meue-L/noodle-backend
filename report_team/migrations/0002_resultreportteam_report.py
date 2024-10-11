# Generated by Django 5.1.1 on 2024-10-11 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_rename_writer_resultreport_creator'),
        ('report_team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultreportteam',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='report.resultreport'),
            preserve_default=False,
        ),
    ]