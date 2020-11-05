# Generated by Django 3.0.7 on 2020-11-05 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_user_department'),
        ('repo', '0006_auto_20201105_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDepartmentMapping',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
