# Generated by Django 3.2 on 2021-04-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0004_alter_purchase_date_yyyymmdd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='GI_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
