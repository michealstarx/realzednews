# Generated by Django 4.1.3 on 2024-04-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_hottest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hottest',
            name='views',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
