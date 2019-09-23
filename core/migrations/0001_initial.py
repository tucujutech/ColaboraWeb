# Generated by Django 2.2 on 2019-09-23 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizacionalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, unique=True)),
                ('nascimento', models.DateField()),
                ('rg', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=12)),
                ('telefone', models.CharField(max_length=13)),
                ('cnh', models.CharField(max_length=12)),
                ('cnh_tipo', models.CharField(default='Não Possui', max_length=12)),
                ('sexo_choices', models.CharField(max_length=2)),
                ('foto_colaborador', models.BinaryField(editable=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacionalApp.Departamento')),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacionalApp.Funcao')),
            ],
            options={
                'db_table': 'Colaborador',
            },
        ),
        migrations.CreateModel(
            name='TipoFormacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_formacao', models.CharField(max_length=13, unique=True)),
            ],
            options={
                'db_table': 'Tipo_Formacao',
            },
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=50)),
                ('instituicao', models.CharField(max_length=50)),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Colaborador', to_field='nome')),
                ('tipo_formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoFormacao', to_field='tipo_formacao')),
            ],
            options={
                'db_table': 'Formacao',
            },
        ),
    ]
