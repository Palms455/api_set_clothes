# Generated by Django 3.0.4 on 2020-03-05 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artmax', '0010_auto_20200305_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='products_ptr',
        ),
        migrations.RemoveField(
            model_name='itemset',
            name='products_ptr',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='item',
            name='producten_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='artmax.Producten'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemset',
            name='producten_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='artmax.Producten'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allitem',
            name='items',
            field=models.ManyToManyField(to='artmax.Producten'),
        ),
    ]
