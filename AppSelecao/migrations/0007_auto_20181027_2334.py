# Generated by Django 2.1.2 on 2018-10-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSelecao', '0006_auto_20181025_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='quarta_saida',
            field=models.BooleanField(null=True, verbose_name='Saída Quarta-Feira'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='quinta_saida',
            field=models.BooleanField(null=True, verbose_name='Saída Quinta-Feira'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='segunda_saida',
            field=models.BooleanField(null=True, verbose_name='Saída Segunda-Feira'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='sexta_saida',
            field=models.BooleanField(null=True, verbose_name='Saída Sexta-Feira'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='terca_saida',
            field=models.BooleanField(null=True, verbose_name='Saída Terça-Feira'),
        ),
    ]