# Generated by Django 3.1.13 on 2021-12-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leases', '0008_lease_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='ed_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lease',
            name='st_date',
            field=models.DateField(),
        ),
    ]
