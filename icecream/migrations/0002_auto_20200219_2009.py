# Generated by Django 3.0.3 on 2020-02-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='available',
            field=models.CharField(choices=[('seasonal', 'seasonal'), ('weekly', 'weekly'), ('daily', 'daily')], max_length=255),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='base',
            field=models.CharField(choices=[('chocalate', 'chocolate'), ('vanilla', 'vanilla')], max_length=255),
        ),
    ]
