# Generated by Django 3.0.7 on 2020-07-26 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repo', '0012_auto_20200726_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Lab'),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Qty', models.IntegerField()),
                ('software_no', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=30)),
                ('bill_no', models.CharField(max_length=10)),
                ('supplier', models.TextField()),
                ('invoice', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('gi_no', models.IntegerField(unique=True)),
                ('rate', models.FloatField()),
                ('Status', models.CharField(max_length=60)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LabFacultyMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('semester', models.IntegerField()),
                ('total_load', models.CharField(max_length=10)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('faculty_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_department', to='repo.Department')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Lab')),
                ('subject_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_department', to='repo.Department')),
            ],
        ),
    ]
