# Generated by Django 5.0 on 2023-12-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_funcionario_cdp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cdp',
            field=models.CharField(default='', max_length=255),
        ),
    ]
