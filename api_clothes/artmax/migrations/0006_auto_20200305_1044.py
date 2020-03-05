# Generated by Django 3.0.4 on 2020-03-05 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artmax', '0005_auto_20200305_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemset',
            name='bottom',
            field=models.OneToOneField(limit_choices_to={'ItemSet_bottom__isnull': 'True', 'type': 'bottom'}, on_delete=django.db.models.deletion.CASCADE, related_name='ItemSet_bottom', to='artmax.Item', verbose_name='Низ'),
        ),
        migrations.AlterField(
            model_name='itemset',
            name='top',
            field=models.OneToOneField(limit_choices_to={'ItemSet_top__isnull': 'True', 'type': 'top'}, on_delete=django.db.models.deletion.CASCADE, related_name='ItemSet_top', to='artmax.Item', verbose_name='Верх'),
        ),
    ]