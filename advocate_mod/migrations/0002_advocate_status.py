# Generated by Django 3.2.7 on 2024-01-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_mod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='status',
            field=models.CharField(default='waiting for approval', max_length=30),
        ),
    ]
