# Generated by Django 3.2.16 on 2022-11-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
