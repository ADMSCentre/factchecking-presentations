# Generated by Django 3.2.5 on 2022-10-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0007_auto_20221019_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyrecord',
            name='demographic_data',
            field=models.TextField(blank=True),
        ),
    ]
