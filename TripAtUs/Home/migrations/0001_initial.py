# Generated by Django 2.0.7 on 2020-04-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlacesToVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travellingWith', models.CharField(max_length=90)),
                ('Culture_Architectural', models.CharField(max_length=90)),
                ('SightSeeing', models.CharField(max_length=90)),
                ('Natural', models.CharField(max_length=90)),
                ('Shopping', models.CharField(max_length=90)),
                ('Outdoor', models.CharField(max_length=90)),
                ('funThingsToDo', models.CharField(max_length=90)),
                ('timeSpent', models.ImageField(max_length=90, upload_to='')),
                ('Locations', models.TextField()),
                ('Latitudes', models.TextField()),
                ('Longitudes', models.TextField()),
            ],
        ),
    ]
