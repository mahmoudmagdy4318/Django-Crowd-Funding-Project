# Generated by Django 2.1.7 on 2020-03-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fbprofile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]