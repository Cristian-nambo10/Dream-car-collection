# Generated by Django 4.0.6 on 2022-07-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('hp', models.IntegerField()),
                ('torque', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
