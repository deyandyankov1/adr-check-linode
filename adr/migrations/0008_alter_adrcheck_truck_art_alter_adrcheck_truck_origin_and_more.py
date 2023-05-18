# Generated by Django 4.2 on 2023-05-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adr', '0007_alter_adrcheck_truck_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adrcheck',
            name='truck_art',
            field=models.CharField(blank=True, choices=[('P', 'Planne'), ('K', 'Aufbau ohne Kühler'), ('KK', 'Aufbau mit Kühler')], max_length=15),
        ),
        migrations.AlterField(
            model_name='adrcheck',
            name='truck_origin',
            field=models.CharField(blank=True, choices=[('A', 'A-Österreich'), ('HR', 'HR-Kroatien'), ('SK', 'SK-Slowakei'), ('D', 'D-Deutschland'), ('RO', 'RO-Rumänien'), ('PL', 'PL-Polen'), ('BG', 'BG-Bulgarien'), ('CZ', 'CZ-Tschechien'), ('H', 'H-Ungarn'), ('GR', 'EL/GR-Griechenland'), ('I', 'I-Italen'), ('DK', 'DK-Dänemark'), ('EST', 'EST-Estland'), ('FIN', 'Finnland'), ('F', 'F-Frankreich'), ('IRL', 'IRL-Irland'), ('LV', 'LV-Lettland'), ('LT', 'LT-Litauen'), ('L', 'L-Luxemburg'), ('M', 'M-Malta'), ('NL', 'NL-Niederlande'), ('P', 'P-Portugal'), ('S', 'S-schweden'), ('E', 'E-Spanien'), ('CY', 'CY-Zypern')], max_length=20),
        ),
        migrations.AlterField(
            model_name='adrcheck',
            name='type',
            field=models.CharField(blank=True, choices=[('SZ', 'Sattelzug'), ('MW', 'Motorwagen')], max_length=10),
        ),
    ]
