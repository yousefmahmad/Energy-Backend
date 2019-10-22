# Generated by Django 2.2.6 on 2019-10-22 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Renewable_TotalMarketed_LowGrowth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('units', models.TextField()),
                ('description', models.TextField()),
                ('updated', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.TextField()),
                ('quads', models.IntegerField()),
                ('renewable_totalmarketed_lowgrowth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='Energy.Renewable_TotalMarketed_LowGrowth')),
            ],
        ),
    ]