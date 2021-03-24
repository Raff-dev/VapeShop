# Generated by Django 3.1.7 on 2021-03-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210324_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.TextField(unique=True),
        ),
    ]
