# Generated by Django 3.0.4 on 2020-07-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scooter',
            name='city',
            field=models.CharField(choices=[('TA', 'Tel Aviv'), ('RG', 'Ramat Gan'), ('GI', 'Givatayim')], default='TA', max_length=2),
        ),
    ]