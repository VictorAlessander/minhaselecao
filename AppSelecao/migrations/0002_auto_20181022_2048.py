# Generated by Django 2.1.2 on 2018-10-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSelecao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extensionista',
            name='workshop_extensionista',
        ),
        migrations.AddField(
            model_name='extensionista',
            name='workshop_extensionista',
            field=models.ManyToManyField(to='AppSelecao.Workshop'),
        ),
    ]
