# Generated by Django 3.0.7 on 2020-10-30 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('Dep_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('bill_no', models.CharField(max_length=10)),
                ('supplier', models.TextField()),
                ('invoice', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('rate', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('Licenced_Qty', models.IntegerField(null=True)),
                ('software_no', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=30)),
                ('gi_no', models.IntegerField(unique=True)),
                ('Status', models.CharField(default='Ok', max_length=60)),
                ('perchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Perchase')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('lab_number', models.IntegerField(default=0)),
                ('lab_area', models.IntegerField(default=0)),
                ('lab_capacity', models.IntegerField(default=0)),
                ('intercom_no', models.IntegerField(default=0)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Department')),
                ('lab_incharge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('equipment_no', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=100)),
                ('gi_no', models.IntegerField(unique=True)),
                ('Status', models.CharField(max_length=60)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Department')),
                ('lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Lab')),
                ('perchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Perchase')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('Computer_no', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=100)),
                ('gi_no', models.IntegerField(unique=True)),
                ('Status', models.CharField(max_length=60)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('processor', models.CharField(max_length=50)),
                ('installed_software', models.ManyToManyField(to='repo.Software')),
                ('lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Lab')),
                ('perchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repo.Perchase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
