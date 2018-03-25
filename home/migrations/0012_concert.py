# Generated by Django 2.0.2 on 2018-03-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_sponsor_rang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance_date', models.DateTimeField()),
                ('location', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=50)),
                ('subtitle', models.CharField(default='', max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]