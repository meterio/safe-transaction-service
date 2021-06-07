# Generated by Django 3.2.4 on 2021-06-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0039_safel2mastercopy_20210519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='safel2mastercopy',
            options={'ordering': ['tx_block_number'], 'verbose_name_plural': 'Safe L2 master copies'},
        ),
        migrations.AlterModelOptions(
            name='safemastercopy',
            options={'ordering': ['tx_block_number'], 'verbose_name_plural': 'Safe master copies'},
        ),
        migrations.AlterField(
            model_name='ethereumevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='internaltx',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='multisigconfirmation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='safecontractdelegate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
