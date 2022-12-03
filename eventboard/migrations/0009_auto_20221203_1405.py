# Generated by Django 3.2.16 on 2022-12-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventboard', '0008_alter_post_event_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Sport'), ('2', 'Business'), ('3', 'Family'), ('4', 'Hobby'), ('5', 'Holiday'), ('6', 'Outdoors'), ('7', 'Music'), ('8', 'Festival')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='county',
            field=models.CharField(blank=True, choices=[('1', 'Carlow'), ('2', 'Cavan'), ('3', 'Clare'), ('4', 'Cork'), ('5', 'Donegal'), ('6', 'Dublin'), ('7', 'Galway'), ('8', 'Kerry'), ('9', 'Kildare'), ('10', 'Kilkenny'), ('11', 'Laois'), ('12', 'Leitrim'), ('13', 'Limerick'), ('14', 'Longford'), ('15', 'Louth'), ('16', 'Mayo'), ('17', 'Meath'), ('18', 'Monaghan'), ('19', 'Offaly'), ('20', 'Roscommon'), ('21', 'Sligo'), ('22', 'Tipperary'), ('23', 'Waterford'), ('24', 'Westmeath'), ('25', 'Wexford'), ('26', 'Wicklow')], max_length=200),
        ),
    ]