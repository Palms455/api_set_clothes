# Generated by Django 3.0.4 on 2020-03-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наменование')),
                ('type', models.CharField(choices=[('top', 'Верх'), ('bottom', 'Низ'), ('not select', 'Не выбрано')], max_length=10, verbose_name='Тип товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ItemSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование набора')),
                ('bottom', models.OneToOneField(limit_choices_to={'ItemSet_bottom__isnull': 'True', 'type': 'bottom'}, on_delete=django.db.models.deletion.CASCADE, related_name='ItemSet_bottom', to='artmax.Item', verbose_name='Низ')),
                ('top', models.OneToOneField(limit_choices_to={'ItemSet_top__isnull': True, 'type': 'top'}, on_delete=django.db.models.deletion.CASCADE, related_name='ItemSet_top', to='artmax.Item', verbose_name='Верх')),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Наборы',
            },
        ),
    ]
