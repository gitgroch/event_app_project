# Generated by Django 3.2.16 on 2022-12-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventboard', '0005_auto_20221202_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='county',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
