# Generated by Django 4.2.3 on 2023-09-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_historique_cumul_panne_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Total',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='nom_equip',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='tache_effectuer',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='executant',
            field=models.CharField(choices=[('Mecanicien', 'Mecanicien'),('Chauffeur', 'Chauffeur'),('Electricien', 'Electricien'),], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='frequence',
            field=models.CharField(choices=[('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Trimestriel', 'Trimestriel'), ('Semestriel', 'Semestriel'), ('Annuel', 'Annuel')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='observations',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='operation',
            field=models.CharField(max_length=700, null=True),
        ),
    ]
