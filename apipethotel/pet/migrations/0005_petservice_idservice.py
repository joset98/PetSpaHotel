# Generated by Django 3.0.3 on 2020-03-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_auto_20200301_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='petservice',
            name='idService',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
