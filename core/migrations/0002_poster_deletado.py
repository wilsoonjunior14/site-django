# Generated by Django 2.2.2 on 2019-07-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='deletado',
            field=models.BooleanField(default=False),
        ),
    ]
