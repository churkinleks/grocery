# Generated by Django 4.2.16 on 2024-09-19 18:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Catalog', 'verbose_name_plural': 'Catalogs'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'Promotion', 'verbose_name_plural': 'Promotions'},
        ),
        migrations.AlterUniqueTogether(
            name='catalog',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='catalog',
            name='top_catalog',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='subcatalogs',
                to='shop.catalog',
                verbose_name='Top catalog',
            ),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='products',
                to='shop.catalog',
                verbose_name='Catalog',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                default='products/images/default.jpg',
                upload_to='products/images',
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=('jpg', 'png'), message="Can only be saved in 'jpg' or 'png' format"
                    )
                ],
                verbose_name='Image',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name='Price',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.FileField(
                default=None,
                null=True,
                upload_to='products/specifications',
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=('pdf',), message="Can only be saved in 'pdf' format"
                    )
                ],
                verbose_name='Specification',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='price',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name='Price',
            ),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='products',
            field=models.ManyToManyField(related_name='promotions', to='shop.product', verbose_name='Products'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AddConstraint(
            model_name='catalog',
            constraint=models.UniqueConstraint(
                fields=('title', 'top_catalog'), name='catalog_unique_title_top_catalog'
            ),
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='upper_catalog',
        ),
    ]
