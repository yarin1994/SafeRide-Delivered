# Generated by Django 3.0.4 on 2020-07-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200716_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vendor', models.BooleanField(default=False)),
            ],
        ),
    ]
