# Generated by Django 3.2.5 on 2022-10-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0005_auto_20220921_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyrecord',
            name='questionnaire_data',
            field=models.TextField(blank=True),
        ),
    ]