# Generated by Django 5.1 on 2024-08-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskenddate',
            field=models.DateTimeField(null=True),
        ),
    ]
