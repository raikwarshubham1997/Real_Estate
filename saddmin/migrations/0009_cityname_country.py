# Generated by Django 4.1 on 2022-09-13 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saddmin', '0008_postequiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityname',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saddmin.country'),
        ),
    ]