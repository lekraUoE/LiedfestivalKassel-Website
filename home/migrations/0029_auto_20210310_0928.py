# Generated by Django 2.0.2 on 2021-03-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_ticketreservation2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketReservation2021',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anrede', models.IntegerField(choices=[(1, 'Herr'), (2, 'Frau'), (3, '—')], default=1)),
                ('titel', models.CharField(blank=True, default='', max_length=15)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('strasse', models.CharField(default='', max_length=50)),
                ('hausnummer', models.CharField(default='', max_length=4)),
                ('plz', models.CharField(default='', max_length=5)),
                ('ort', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(blank=True, default='', max_length=20)),
                ('tickets_gesamtpaket', models.PositiveIntegerField(default=0)),
                ('tickets_eroeffnung', models.PositiveIntegerField(default=2)),
                ('tickets_eroeffnung_erm', models.PositiveIntegerField(default=0)),
                ('tickets_winterreise', models.PositiveIntegerField(default=2)),
                ('tickets_winterreise_erm', models.PositiveIntegerField(default=0)),
                ('tickets_liederabend', models.PositiveIntegerField(default=2)),
                ('tickets_liederabend_erm', models.PositiveIntegerField(default=0)),
                ('tickets_jungeslied', models.PositiveIntegerField(default=2)),
                ('tickets_jungeslied_erm', models.PositiveIntegerField(default=0)),
                ('tickets_muellerin', models.PositiveIntegerField(default=2)),
                ('tickets_muellerin_erm', models.PositiveIntegerField(default=0)),
                ('tickets_abschluss', models.PositiveIntegerField(default=2)),
                ('tickets_abschluss_erm', models.PositiveIntegerField(default=0)),
                ('tickets_summe', models.FloatField(blank=True, default=0.0, null=True)),
                ('nachricht', models.TextField(blank=True, default='')),
                ('request_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_abschluss',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_eroeffnung',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_jungeslied',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_liederabend',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_muellerin',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketreservation2020',
            name='tickets_winterreise',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
