# Generated by Django 5.0.3 on 2024-03-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_tasks', '0002_rename_maintenace_tasks_maintenance_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance_tasks',
            name='status',
            field=models.CharField(default='Pendiente'),
        ),
    ]