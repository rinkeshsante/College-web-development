# Generated by Django 3.2 on 2021-04-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_auto_20210410_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateField(),
        ),
    ]
