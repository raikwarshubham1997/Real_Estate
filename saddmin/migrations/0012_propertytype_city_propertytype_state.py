# Generated by Django 4.1 on 2022-09-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saddmin', '0011_rename_country_cityname_country_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertytype',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='propertytype',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
