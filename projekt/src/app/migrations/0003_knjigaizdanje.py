# Generated by Django 3.0.6 on 2020-05-24 12:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200523_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnjigaIzdanje',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unikatan id za knjigu', primary_key=True, serialize=False)),
                ('izdanje', models.CharField(max_length=200)),
                ('vracanje', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('u', 'U pripravnosti'), ('p', 'Posudjena'), ('d', 'Dostupna'), ('r', 'Rezervirana')], default='m', help_text='Dostupnost knjige', max_length=1)),
                ('knjiga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Knjiga')),
            ],
            options={
                'ordering': ['vracanje'],
            },
        ),
    ]
