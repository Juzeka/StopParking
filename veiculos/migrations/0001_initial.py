# Generated by Django 4.0.5 on 2022-07-11 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('cor', models.CharField(max_length=15)),
                ('observacoes', models.TextField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo_marca', to='veiculos.marca', verbose_name='Marca')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculo_pessoa', to='core.pessoa', verbose_name='Propietario')),
            ],
        ),
    ]
