# Generated by Django 2.2.2 on 2019-09-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name_company',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='nit',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(default='', max_length=32),
        ),
    ]
