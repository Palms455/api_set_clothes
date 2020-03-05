# Generated by Django 3.0.4 on 2020-03-05 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artmax', '0004_auto_20200305_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemset',
            name='top',
            field=models.OneToOneField(limit_choices_to={'ItemSet_top__isnull': 'True', 'type': 'top'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ItemSet_top', to='artmax.Item', verbose_name='Верх'),
        ),
    ]