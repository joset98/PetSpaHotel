# Generated by Django 3.0.3 on 2020-03-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_petservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petservice',
            name='fecha',
            field=models.DateField(max_length=50),
        ),
    ]
