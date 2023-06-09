# Generated by Django 4.2 on 2023-04-30 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SignatureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_date', models.DateTimeField(blank=True, null=True, verbose_name='Signature date')),
                ('signature', jsignature.fields.JSignatureField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdrCheck',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('adr_card', models.CharField(max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('truck_plate1', models.CharField(max_length=25)),
                ('truck_plate2', models.CharField(max_length=25)),
                ('truck_origin', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('SZ', 'Sattelzug'), ('MW', 'Motorwagen')], max_length=10)),
                ('truck_art', models.CharField(choices=[('P', 'Planne'), ('K', 'Aufbau ohne Kühler'), ('KK', 'Aufbau mit Kühler')], default='P', max_length=15)),
                ('field1', models.CharField(blank=True, max_length=25, null=True)),
                ('field2', models.CharField(blank=True, max_length=25, null=True)),
                ('check_1', models.BooleanField(default=False)),
                ('check_2', models.BooleanField(default=False)),
                ('check_3', models.BooleanField(default=False)),
                ('check_4', models.BooleanField(default=False)),
                ('check_5', models.BooleanField(default=False)),
                ('check_6', models.BooleanField(default=False)),
                ('check_7', models.BooleanField(default=False)),
                ('check_8', models.BooleanField(default=False)),
                ('check_9', models.BooleanField(default=False)),
                ('check_10', models.BooleanField(default=False)),
                ('check_11', models.BooleanField(default=False)),
                ('check_12', models.BooleanField(default=False)),
                ('check_13', models.BooleanField(default=False)),
                ('check_14', models.BooleanField(default=False)),
                ('check_15', models.BooleanField(default=False)),
                ('check_16', models.BooleanField(default=False)),
                ('check_17', models.BooleanField(default=False)),
                ('check_18', models.BooleanField(default=False)),
                ('check_19', models.BooleanField(default=False)),
                ('check_20', models.BooleanField(default=False)),
                ('check_21', models.BooleanField(default=False)),
                ('check_22', models.BooleanField(default=False)),
                ('check_23', models.BooleanField(default=False)),
                ('check_24', models.BooleanField(default=False)),
                ('check_25', models.BooleanField(default=False)),
                ('check_26', models.BooleanField(default=False)),
                ('check_27', models.BooleanField(default=False)),
                ('check_28', models.BooleanField(default=False)),
                ('check_29', models.BooleanField(default=False)),
                ('check_30', models.BooleanField(default=False)),
                ('check_31', models.BooleanField(default=False)),
                ('check_32', models.BooleanField(default=False)),
                ('check_33', models.BooleanField(default=False)),
                ('check_34', models.BooleanField(default=False)),
                ('check_35', models.BooleanField(default=False)),
                ('check_36', models.BooleanField(default=False)),
                ('check_37', models.BooleanField(default=False)),
                ('check_38', models.BooleanField(default=False)),
                ('check_39', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['complete'],
            },
        ),
    ]
