# Generated by Django 3.1.7 on 2021-03-22 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210228_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('NA', 'Not Applicable')], default=('NA', 'Not Applicable'), max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['product__collection__created_at', 'product__category__name', 'name']},
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='instance',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='products.variant'),
        ),
        migrations.AlterUniqueTogether(
            name='instance',
            unique_together={('size', 'variant')},
        ),
    ]
