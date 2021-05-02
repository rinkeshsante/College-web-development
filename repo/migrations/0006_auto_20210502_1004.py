# Generated by Django 3.2 on 2021-05-02 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0005_alter_purchase_gi_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Other_Info',
            new_name='Remarks',
        ),
        migrations.AddField(
            model_name='item',
            name='Located_since',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
