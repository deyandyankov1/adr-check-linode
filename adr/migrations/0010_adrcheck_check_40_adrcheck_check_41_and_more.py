# Generated by Django 4.2 on 2023-05-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adr', '0009_alter_adrcheck_field1'),
    ]

    operations = [
        migrations.AddField(
            model_name='adrcheck',
            name='check_40',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adrcheck',
            name='check_41',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adrcheck',
            name='check_42',
            field=models.BooleanField(default=False),
        ),
    ]