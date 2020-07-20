# Generated by Django 2.2.8 on 2020-07-17 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SDUser',
            fields=[
                ('nickname', models.CharField(blank=True, default='', max_length=30)),
                ('name', models.CharField(default='', max_length=50)),
                ('picture', models.CharField(default='', max_length=200)),
                ('last_updated', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('RO', 'Restaurant Owner'), ('BU', 'Basic User')], default='BU', max_length=5)),
                ('restaurant_id', models.CharField(blank=True, default=None, max_length=24)),
            ],
        ),
    ]