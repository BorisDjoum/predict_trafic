# Generated by Django 4.2.3 on 2023-09-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_historique_panne_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='frequence',
            field=models.CharField(choices=[('Journalier', 'Journalier'), ('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Trimestriel', 'Trimestriel'), ('Semestriel', 'Semestriel'), ('Annuel', 'Annuel')], max_length=50, null=True),
        ),
    ]
