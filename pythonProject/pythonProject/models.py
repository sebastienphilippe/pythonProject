from django.db import models

# Create your models here.


class Organization(models.Model):

    __source__ = "ProjetPython/projet/p1/data/newdataH.csv"

    representants_id = models.IntegerField(
        verbose_name='representants_id', primary_key=True)
    date_premiere_publication = models.DateTimeField(
        verbose_name='date_premiere_publication')
    declaration_organisation_appartenance = models.BooleanField(
        verbose_name='declaration_organisation_appartenance')
    declaration_tiers = models.BooleanField(verbose_name='declaration_tiers')
    denomination = models.CharField(verbose_name='denomination', max_length=30)
    identifiant_national = models.IntegerField(
        verbose_name='identifiant_national')
    activites_publiees = models.BooleanField(verbose_name='activites_publiees')
    type_identifiant_national = models.CharField(
        verbose_name='type_identifiant_national', max_length=30)
    exercices_id = models.IntegerField(verbose_name='exercices_id')
    date_debut = models.DateField(verbose_name='date_debut')
    date_fin = models.DateField(verbose_name='date_fin')
    exercice_sans_activite = models.BooleanField(
        verbose_name='exercice_sans_activite')
    nombre_activites = models.IntegerField(verbose_name='nombre_activites')
    declaration_incomplete = models.BooleanField(
        verbose_name='declaration_incomplete')
    date_publication = models.DateField(verbose_name='date_publication')
    exercice_sans_CA = models.CharField(
        verbose_name='exercice_sans_CA', max_length=30)
    montant_depense = models.CharField(
        verbose_name='montant_depense', max_length=30)
    nombre_salaries = models.FloatField(verbose_name='nombre_salaries',)
    chiffre_affaires = models.CharField(
        verbose_name='chiffre_affaires', max_length=30)
    annee_debut = models.IntegerField(verbose_name='annee_debut')
    annee_fin = models.IntegerField(verbose_name='annee_fin')
    montant_depense_inf = models.IntegerField(
        verbose_name='montant_depense_inf')
    montant_depense_sup = models.IntegerField(
        verbose_name='montant_depense_sup')
    ca_inf = models.IntegerField(verbose_name='ca_inf')
    ca_sup = models.FloatField(verbose_name='ca_sup')
    activite_id = models.FloatField(verbose_name='activite_id')
    date_publication_activite = models.DateField(
        verbose_name='date_publication_activite')
    identifiant_fiche = models.CharField(
        verbose_name='identifiant_fiche', max_length=30)
    objet_activite = models.CharField(
        verbose_name='objet_activite', max_length=30)
    domaines_intervention_actions_menees = models.CharField(
        verbose_name='domaines_intervention_actions_menees', max_length=30)
    action_representation_interet_id = models.FloatField(
        verbose_name='action_representation_interet_id')
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
