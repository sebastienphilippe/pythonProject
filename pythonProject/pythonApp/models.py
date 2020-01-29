from django.db import models

# Create your models here.
# import pandas as pd
# data = pd.read_csv("vueFusionnees/2_actions.csv")

class Organization(models.Model):

  


class Clients(models.Model):

    representants_id = models.ForeignKey(representants_id, on_delete=models.CASCADE, primary_key=True)
    denomination_client = models.CharField(verbose_name='denomination_client',max_length=30)
    identifiant_national_client = models.CharField(verbose_name='identifiant_national_client',max_length=30)
    type_identifiant_national_client = models.CharField(verbose_name='type_identifiant_national_client',max_length=30)

class Affiliations(models.Model):
    representants_id = models.ForeignKey(representants_id, on_delete=models.CASCADE, primary_key=True)
    denomination_affiliation = models.CharField(verbose_name='denomination_affiliation',max_length=30)
    identifiant_national_client = models.CharField(verbose_name='identifiant_national_client',max_length=30)
    type_identifiant_national_client = models.CharField(verbose_name='type_identifiant_national_client',max_length=30)

class NiveauxIntervention(models.Model):
    niveau_intervention  = models.CharField(verbose_name='niveau_intervention',max_length=30)
    representants_id = models.ForeignKey(representants_id, on_delete=models.CASCADE, primary_key=True)

class Exercices(models.Model):
     exercices_id = models.IntegerField(verbose_name='exercices_id', primary_key=True)
     representants_id = models.ForeignKey(representants_id, on_delete=models.CASCADE)
     date_debut = models.CharField(verbose_name='date_debut',max_length=30)
     date_fin = models.CharField(verbose_name='date_fin',max_length=30)
     exercice_sans_activite = models.BooleanField(verbose_name='exercice_sans_activite')
     nombre_activites = models.IntergerField(verbose_name='nombre_activites',max_length=30)
     declaration_incomplete = models.BooleanField(verbose_name='declaration_incomplete',max_length=3)
     date_publication = models.CharField(verbose_name='date_publication',max_length=30)
     exercice_sans_CA = models.BooleanField(verbose_name='exercice_sans_CA')
     montant_depense = models.CharField(verbose_name='montant_depense',max_length=30)
     nombre_salaries = models.IntegerField(verbose_name='nombre_salaries',max_length=30)
     chiffre_affaires = models.CharField(verbose_name='chiffre_affaires',max_length=30)
     annee_debut = models.CharField(verbose_name='annee_debut',max_length=30)
     annee_fin = models.CharField(verbose_name='annee_fin',max_length=30)
     montant_depense_inf = models.IntegerField(verbose_name='montant_depense_inf',max_length=30)
     montant_depense_sup = models.IntegerField(verbose_name='montant_depense_sup',max_length=30)
     ca_inf = models.FloatField(verbose_name='ca_inf',max_length=30)
     ca_sup = models.CharField(verbose_name='ca_sup',max_length=30)
