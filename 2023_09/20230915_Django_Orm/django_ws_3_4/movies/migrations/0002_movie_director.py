# Generated by Django 4.2.5 on 2023-09-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]
