# Generated by Django 3.1.7 on 2021-02-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210228_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Collection',
            new_name='collection',
        ),
    ]