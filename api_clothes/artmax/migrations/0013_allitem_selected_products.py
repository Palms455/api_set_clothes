# Generated by Django 3.0.4 on 2020-03-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artmax', '0012_auto_20200305_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='allitem',
            name='selected_products',
            field=models.CharField(default='all_product_items', max_length=150),
            preserve_default=False,
        ),
    ]
