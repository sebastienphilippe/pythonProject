# Generated by Django 3.0 on 2020-01-31 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonApp', '0006_auto_20200131_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercices',
            fields=[
                ('exercices_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='exercices_id')),
                ('date_debut', models.CharField(max_length=30, verbose_name='date_debut')),
                ('date_fin', models.CharField(max_length=30, verbose_name='date_fin')),
                ('exercice_sans_activite', models.CharField(max_length=30, verbose_name='exercice_sans_activite')),
                ('nombre_activites', models.IntegerField(verbose_name='nombre_activites')),
                ('declaration_incomplete', models.CharField(max_length=3, verbose_name='declaration_incomplete')),
                ('date_publication', models.CharField(max_length=30, verbose_name='date_publication')),
                ('exercice_sans_CA', models.CharField(max_length=30, verbose_name='exercice_sans_CA')),
                ('montant_depense', models.CharField(max_length=30, verbose_name='montant_depense')),
                ('nombre_salaries', models.CharField(max_length=30, verbose_name='nombre_salaries')),
                ('chiffre_affaires', models.CharField(max_length=30, verbose_name='chiffre_affaires')),
                ('annee_debut', models.CharField(max_length=30, verbose_name='annee_debut')),
                ('annee_fin', models.CharField(max_length=30, verbose_name='annee_fin')),
                ('montant_depense_inf', models.CharField(max_length=30, verbose_name='montant_depense_inf')),
                ('montant_depense_sup', models.CharField(max_length=30, verbose_name='montant_depense_sup')),
                ('ca_inf', models.FloatField(max_length=30, verbose_name='ca_inf')),
                ('ca_sup', models.CharField(max_length=30, verbose_name='ca_sup')),
            ],
        ),
        migrations.CreateModel(
            name='Objets_activites',
            fields=[
                ('activite_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='activite_id')),
                ('date_publication_activite', models.CharField(blank=True, max_length=30, null=True)),
                ('identifiant_fiche', models.CharField(blank=True, max_length=30, null=True)),
                ('objet_activite', models.CharField(blank=True, max_length=30, null=True)),
                ('exercices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Exercices')),
            ],
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='representants_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='representants_id'),
        ),
        migrations.CreateModel(
            name='Secteur_activites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secteur_activite', models.CharField(max_length=30, verbose_name='secteur_activite')),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('action_representation_interet_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='activite_id')),
                ('observation', models.CharField(max_length=30, verbose_name='domaineIntervention')),
                ('activite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Objets_activites')),
            ],
        ),
        migrations.CreateModel(
            name='Niveaux_intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_intervention', models.CharField(max_length=30, verbose_name='niveau_intervention')),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Ministeres_aai_api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable_public', models.CharField(max_length=30, verbose_name='responsable_public')),
                ('departement_ministeriel', models.CharField(max_length=30, verbose_name='departement_ministeriel')),
                ('responsable_public_ou_dpt_ministeriel_autre', models.CharField(max_length=30, verbose_name='responsable_public_ou_dpt_ministeriel_autre')),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Observations')),
            ],
        ),
        migrations.AddField(
            model_name='exercices',
            name='representants_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales'),
        ),
        migrations.CreateModel(
            name='Domaines_intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domaineIntervention', models.CharField(max_length=30, verbose_name='domaineIntervention')),
                ('activite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Objets_activites')),
            ],
        ),
        migrations.CreateModel(
            name='Dirigeants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite_dirigeant', models.CharField(blank=True, max_length=13, null=True)),
                ('fonction_dirigeant', models.CharField(blank=True, max_length=119, null=True)),
                ('nom_dirigeant', models.CharField(blank=True, max_length=39, null=True)),
                ('prenom_dirigeant', models.CharField(blank=True, max_length=31, null=True)),
                ('nom_prenom_dirigeant', models.CharField(blank=True, max_length=45, null=True)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Decisions_concernees',
            fields=[
                ('Decisions_concernees', models.IntegerField(primary_key=True, serialize=False, verbose_name='activite_id')),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Observations')),
            ],
        ),
        migrations.CreateModel(
            name='Collaborateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite_collaborateur', models.CharField(max_length=30, verbose_name='civilite_collaborateur')),
                ('fonction_collaborateur', models.CharField(max_length=30, verbose_name='fonction_collaborateur')),
                ('nom_collaborateur', models.CharField(max_length=30, verbose_name='nom_collaborateur')),
                ('prenom_collaborateur', models.CharField(max_length=30, verbose_name='prenom_collaborateur')),
                ('nom_prenom_collaborateur', models.CharField(max_length=30, verbose_name='nom_prenom_collaborateur')),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination_client', models.CharField(max_length=30, verbose_name='denomination_client')),
                ('identifiant_national_client', models.CharField(max_length=30, verbose_name='identifiant_national_client')),
                ('type_identifiant_national_client', models.CharField(max_length=30, verbose_name='type_identifiant_national_client')),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaire_action_menee', models.CharField(max_length=30, verbose_name='beneficiaire_action_menee')),
                ('action_menee_en_propre', models.CharField(max_length=30, verbose_name='action_menee_en_propre')),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Observations')),
            ],
        ),
        migrations.CreateModel(
            name='Affiliations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination_affiliation', models.CharField(max_length=30, verbose_name='denomination_affiliation')),
                ('identifiant_national_client', models.CharField(max_length=30, verbose_name='identifiant_national_client')),
                ('type_identifiant_national_client', models.CharField(max_length=30, verbose_name='type_identifiant_national_client')),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Informations_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Actions_menees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_menee', models.CharField(max_length=30, verbose_name='action_menee')),
                ('action_menee_autre', models.CharField(max_length=30, verbose_name='action_menee_autre')),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythonApp.Observations')),
            ],
        ),
    ]
