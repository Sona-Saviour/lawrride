# Generated by Django 3.2.7 on 2024-02-08 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_mod', '0004_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_mod.user'),
        ),
    ]