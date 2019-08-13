# Generated by Django 2.2.4 on 2019-08-13 15:54

import apps.base.validador
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100, validators=[apps.base.validador.validate_cnpj], verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=300, verbose_name='razão social')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('telefone', models.CharField(blank=True, max_length=100, null=True, verbose_name='telefone')),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
                'db_table': 'empresa',
            },
        ),
    ]
