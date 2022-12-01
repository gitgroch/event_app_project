# Generated by Django 3.2.16 on 2022-12-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventboard', '0002_alter_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_date_and_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_location',
            field=models.TextField(max_length=200),
        ),
    ]