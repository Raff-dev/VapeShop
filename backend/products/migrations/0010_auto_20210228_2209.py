# Generated by Django 3.1.7 on 2021-02-28 21:09

from django.db import migrations, models
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210228_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-collection__created_at', 'category__name']},
        ),
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='collection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='product_images/default_product_image.png', upload_to=products.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='variant',
            name='name',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='variant',
            unique_together={('name', 'product')},
        ),
    ]
