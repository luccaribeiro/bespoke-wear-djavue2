# Generated by Django 4.0.5 on 2023-02-08 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
