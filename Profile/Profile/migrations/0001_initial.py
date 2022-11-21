# Generated by Django 4.1.3 on 2022-11-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5)),
                ('birthday', models.DateField(null=True)),
                ('address', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('graduate_yr', models.DateField(null=True)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]