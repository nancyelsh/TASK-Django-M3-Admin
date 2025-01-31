# Generated by Django 4.0.4 on 2023-02-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_alter_pokemon_modified_at_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('EL', 'ELECTRIC'), ('FA', 'FAIRY'), ('WA', 'WATER'), ('GH', 'GHOST'), ('GR', 'GRASS'), ('ST', 'STEEL')], default='WATER', max_length=250),
        ),
    ]
