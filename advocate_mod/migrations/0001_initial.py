# Generated by Django 3.2.7 on 2024-01-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('about', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='advocates')),
            ],
        ),
    ]