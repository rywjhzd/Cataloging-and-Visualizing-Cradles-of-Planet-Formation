# Generated by Django 2.2.6 on 2019-11-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=100, verbose_name='object')),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='category')),
                ('ra', models.CharField(blank=True, max_length=100, null=True, verbose_name='ra')),
                ('dec', models.CharField(blank=True, max_length=100, null=True, verbose_name='dec')),
                ('distance', models.CharField(blank=True, max_length=100, null=True, verbose_name='distance')),
                ('system_age', models.CharField(blank=True, max_length=100, null=True, verbose_name='system_age')),
                ('central_star_mass', models.CharField(blank=True, max_length=100, null=True, verbose_name='central_star_mass')),
                ('disk_major_axis', models.CharField(blank=True, max_length=100, null=True, verbose_name='disk_major_axis')),
                ('inclination', models.CharField(blank=True, max_length=100, null=True, verbose_name='inclination')),
                ('references', models.CharField(blank=True, max_length=10, null=True, verbose_name='references')),
                ('catalog', models.CharField(blank=True, max_length=20, null=True, verbose_name='catalog')),
            ],
            options={
                'verbose_name': 'disk',
                'verbose_name_plural': 'disks',
                'ordering': ('object',),
            },
        ),
    ]
