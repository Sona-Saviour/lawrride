# Generated by Django 3.2.7 on 2024-02-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_mod', '0004_alter_advocate_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='about',
            field=models.CharField(max_length=1000),
        ),
    ]
