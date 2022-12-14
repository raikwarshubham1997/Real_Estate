# Generated by Django 4.1 on 2022-09-12 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saddmin', '0007_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='postEquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('property_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saddmin.propertytype')),
            ],
        ),
    ]
