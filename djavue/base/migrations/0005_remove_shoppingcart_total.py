# Generated by Django 4.0.5 on 2023-02-09 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='total',
        ),
    ]
