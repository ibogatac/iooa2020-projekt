# Generated by Django 3.0.6 on 2020-05-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200527_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knjigaizdanje',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Posudjena'), ('d', 'Dostupna')], default='d', max_length=1),
        ),
    ]
