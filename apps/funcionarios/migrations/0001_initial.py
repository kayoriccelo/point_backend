# Generated by Django 2.2.4 on 2019-08-14 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jornadas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140, null=True, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, null=True, verbose_name='cpf')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=100, null=True, verbose_name='sexo')),
                ('data_admissao', models.DateTimeField(null=True, verbose_name='data de admissão')),
                ('data_nascimento', models.DateTimeField(null=True, verbose_name='data de nascimento')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='empresa.Empresa', verbose_name='empresa')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='funcionarios', to='jornadas.Jornada', verbose_name='jornada')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'funcionario',
                'verbose_name_plural': 'funcionarios',
                'db_table': 'funcionario',
            },
        ),
    ]
