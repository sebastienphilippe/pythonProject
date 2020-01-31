# Generated by Django 3.0 on 2020-01-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonApp', '0003_actions_menees_affiliations_beneficiaires_clients_collaborateurs_decisions_concernees_domaines_inter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='representants_id',
        ),
        migrations.RemoveField(
            model_name='collaborateurs',
            name='representants_id',
        ),
        migrations.RemoveField(
            model_name='dirigeants',
            name='representants_id',
        ),
        migrations.RemoveField(
            model_name='niveaux_intervention',
            name='representants_id',
        ),
        migrations.RemoveField(
            model_name='secteur_activites',
            name='representants_id',
        ),
        migrations.AlterField(
            model_name='exercices',
            name='declaration_incomplete',
            field=models.CharField(max_length=3, verbose_name='declaration_incomplete'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='exercice_sans_CA',
            field=models.CharField(max_length=30, verbose_name='exercice_sans_CA'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='exercice_sans_activite',
            field=models.CharField(max_length=30, verbose_name='exercice_sans_activite'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='montant_depense_inf',
            field=models.CharField(max_length=30, verbose_name='montant_depense_inf'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='montant_depense_sup',
            field=models.CharField(max_length=30, verbose_name='montant_depense_sup'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='nombre_salaries',
            field=models.CharField(max_length=30, verbose_name='nombre_salaries'),
        ),
        migrations.DeleteModel(
            name='Affiliations',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Collaborateurs',
        ),
        migrations.DeleteModel(
            name='Dirigeants',
        ),
        migrations.DeleteModel(
            name='Niveaux_intervention',
        ),
        migrations.DeleteModel(
            name='Secteur_activites',
        ),
    ]