# Generated by Django 3.1 on 2020-09-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile_number',
            field=models.CharField(max_length=13),
        ),
    ]