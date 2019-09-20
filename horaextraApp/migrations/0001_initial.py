# Generated by Django 2.2 on 2019-09-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoraExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('faturado', models.BooleanField()),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Colaborador', to_field='nome')),
            ],
            options={
                'db_table': 'HoraExtra',
            },
        ),
    ]
