# Generated by Django 3.0.8 on 2020-07-05 05:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('birth', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_value', models.FloatField(null=True)),
                ('date_order', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'stock'), (2, 'transferring'), (3, 'delivered'), (4, 'canceled')], default=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Client')),
                ('products', models.ManyToManyField(to='rest.Product')),
            ],
        ),
    ]
