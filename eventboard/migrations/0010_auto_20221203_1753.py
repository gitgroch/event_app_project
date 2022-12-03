# Generated by Django 3.2.16 on 2022-12-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventboard', '0009_auto_20221203_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contact_address',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='post',
            name='contact_website',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Sport', 'Sport'), ('Business', 'Business'), ('Family', 'Family'), ('Hobby', 'Hobby'), ('Holiday', 'Holiday'), ('Outdoors', 'Outdoors'), ('Music', 'Music'), ('Festival', 'Festival'), ('Culture', 'Culture')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='county',
            field=models.CharField(blank=True, choices=[('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Donegal', 'Donegal'), ('Dublin', 'Dublin'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
