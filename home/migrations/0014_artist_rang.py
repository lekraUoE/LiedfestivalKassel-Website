# Generated by Django 2.0.2 on 2018-03-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180324_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='rang',
            field=models.PositiveIntegerField(default=0),
        ),
    ]