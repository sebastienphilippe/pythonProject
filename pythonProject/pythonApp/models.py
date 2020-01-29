from django.db import models

# Create your models here.
# import pandas as pd
# data = pd.read_csv("vueFusionnees/2_actions.csv")

class Infogen(models.Model):

    representants_id = models.IntegerField(
        verbose_name='representants_id', primary_key=True)
    date_premiere_publication = models.CharField(
        verbose_name='date_premiere_publication',max_length=30)
    declaration_organisation_appartenance = models.BooleanField(
        verbose_name='declaration_organisation_appartenance',max_length=30)
    declaration_tiers = models.BooleanField(verbose_name='declaration_tiers',max_length=30)
    denomination = models.CharField(verbose_name='denomination', max_length=30)
    identifiant_national = models.CharField(
        verbose_name='identifiant_national',max_length=30)
    activites_publiees = models.BooleanField(verbose_name='activites_publiees')
    type_identifiant_national = models.CharField(
        verbose_name='type_identifiant_national', max_length=30)
    exercices_id = models.CharField(max_length=30)
    date_debut = models.CharField(verbose_name='date_debut',max_length=30)
    date_fin = models.CharField(verbose_name='date_fin',max_length=30)
    exercice_sans_activite = models.CharField(
        verbose_name='exercice_sans_activite',max_length=30)
    nombre_activites = models.CharField(verbose_name='nombre_activites',max_length=30)
    declaration_incomplete = models.CharField(
        verbose_name='declaration_incomplete',max_length=30)
    date_publication = models.CharField(verbose_name='date_publication',max_length=30)
    exercice_sans_CA = models.CharField(
        verbose_name='exercice_sans_CA', max_length=30)
    montant_depense = models.CharField(
        verbose_name='montant_depense', max_length=30)
    nombre_salaries = models.CharField(verbose_name='nombre_salaries',max_length=30)
    chiffre_affaires = models.CharField(
        verbose_name='chiffre_affaires', max_length=30)
    annee_debut = models.CharField(verbose_name='annee_debut',max_length=30)
    annee_fin = models.CharField(verbose_name='annee_fin',max_length=30)
    montant_depense_inf = models.CharField(
        verbose_name='montant_depense_inf',max_length=30)
    montant_depense_sup = models.CharField(
        verbose_name='montant_depense_sup',max_length=30)
    ca_inf = models.CharField(verbose_name='ca_inf',max_length=30)
    ca_sup = models.CharField(verbose_name='ca_sup',max_length=30)
    activite_id = models.CharField(verbose_name='activite_id',max_length=30)
    date_publication_activite = models.CharField(
        verbose_name='date_publication_activite',max_length=30)
    identifiant_fiche = models.CharField(
        verbose_name='identifiant_fiche', max_length=30)
    objet_activite = models.CharField(
        verbose_name='objet_activite', max_length=30)
    domaines_intervention_actions_menees = models.CharField(
        verbose_name='domaines_intervention_actions_menees', max_length=30)
    action_representation_interet_id = models.CharField(
        verbose_name='action_representation_interet_id',max_length=30)
    responsable_public = models.CharField(
        verbose_name='responsable_public', max_length=30)
    departement_ministeriel = models.CharField(
        verbose_name='departement_ministeriel', max_length=30)
    beneficiaire_action_menee = models.CharField(
        verbose_name='beneficiaire_action_menee', max_length=30)
    action_menee = models.CharField(verbose_name='action_menee', max_length=30)
    decision_concernee = models.CharField(
        verbose_name='decision_concernee', max_length=30)


def __str__(self):
    return self.ref
