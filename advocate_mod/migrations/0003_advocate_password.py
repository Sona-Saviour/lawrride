# Generated by Django 3.2.7 on 2024-02-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_mod', '0002_advocate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
    ]