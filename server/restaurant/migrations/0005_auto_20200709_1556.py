# Generated by Django 2.2.8 on 2020-07-09 19:56

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200709_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='tags',
            field=djongo.models.fields.ListField(blank=True),
        ),
    ]
