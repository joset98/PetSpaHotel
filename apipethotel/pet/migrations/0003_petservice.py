# Generated by Django 3.0.3 on 2020-03-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(max_length=50)),
                ('idPet', models.IntegerField()),
                ('hora', models.DurationField(max_length=50)),
            ],
        ),
    ]
