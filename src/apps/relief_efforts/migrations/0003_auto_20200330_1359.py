# Generated by Django 3.0.4 on 2020-03-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relief_efforts', '0002_auto_20200330_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizations',
            name='relief_type',
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='postal_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
