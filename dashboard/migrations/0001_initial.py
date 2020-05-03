# Generated by Django 3.0.3 on 2020-05-03 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(default='asdf', max_length=50)),
                ('alpha2_code', models.CharField(max_length=2)),
                ('alpha3_code', models.CharField(max_length=3)),
                ('confirmed', models.IntegerField(default=0, verbose_name='confirmed')),
                ('recovered', models.IntegerField(default=0, verbose_name='recovered')),
                ('deaths', models.IntegerField(default=0, verbose_name='deaths')),
                ('mortality', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='mortality')),
                ('last_updated', models.DateField(verbose_name='last_updated')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('confirmed', models.IntegerField(default=0, verbose_name='confirmed')),
                ('recovered', models.IntegerField(default=0, verbose_name='recovered')),
                ('deaths', models.IntegerField(default=0, verbose_name='deaths')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Country')),
            ],
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name', 'alpha2_code'], name='dashboard_c_name_c946c6_idx'),
        ),
        migrations.AddIndex(
            model_name='date',
            index=models.Index(fields=['date', 'country'], name='dashboard_d_date_21fb65_idx'),
        ),
    ]
