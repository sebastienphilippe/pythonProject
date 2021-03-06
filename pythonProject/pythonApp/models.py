from django.db import models

# Create your models here.
# import pandas as pd
# data = pd.read_csv("vueFusionnees/2_actions.csv")

class Informations_generales(models.Model):

    representants_id = models.IntegerField(verbose_name='representants_id', primary_key=True)
    adresse = models.CharField( verbose_name='adresse',max_length=30)
    code_postal = models.CharField(verbose_name='code_postal',max_length=30)
    derniere_publication_activite = models.CharField(verbose_name='derniere_publication_activite',max_length=30)
    date_premiere_publication = models.CharField(verbose_name='date_premiere_publication', max_length=30)
    declaration_organisation_appartenance = models.CharField(verbose_name='declaration_organisation_appartenance',max_length=30)
    declaration_tiers = models.CharField(verbose_name='declaration_tiers', max_length=30)
    denomination = models.CharField(verbose_name='denomination', max_length=30)
    identifiant_national = models.CharField(verbose_name='identifiant_national', max_length=30)
    activites_publiees = models.CharField(verbose_name='activites_publiees',max_length=30)
    page_facebook = models.CharField(verbose_name='page_facebook',max_length=30)
    page_linkedin = models.CharField(verbose_name='page_linkedin',max_length=30)
    page_twitter = models.CharField(verbose_name='page_twitter',max_length=30)
    site_web = models.CharField(verbose_name='site_web',max_length=30)
    nom_usage_HATVP = models.CharField(verbose_name='nom_usage_HATVP',max_length=30)
    pays = models.CharField(verbose_name='pays', max_length=30)
    sigle_HATVP = models.CharField(verbose_name='sigle_HATVP', max_length=30)
    type_identifiant_national = models.CharField(verbose_name='type_identifiant_national',max_length=30)
    ville = models.CharField(verbose_name='ville', max_length=30)
    label_categorie_organisation = models.CharField(verbose_name='label_categorie_organisation',max_length=30)



# class Dirigeants(models.Model):
#     civilite_dirigeant=models.CharField(null=True,blank=True,max_length=13)
#     fonction_dirigeant=models.CharField(null=True,blank=True,max_length=119)
#     nom_dirigeant=models.CharField(null=True,blank=True,max_length=39)
#     prenom_dirigeant=models.CharField(null=True,blank=True,max_length=31)
#     representants_id=models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
#     nom_prenom_dirigeant=models.CharField(null=True,blank=True,max_length=45)


# class Collaborateurs(models.Model):
#     civilite_collaborateur = models.CharField(        verbose_name='civilite_collaborateur',max_length=30)
#     fonction_collaborateur = models.CharField(        verbose_name='fonction_collaborateur',max_length=30)
#     nom_collaborateur = models.CharField(verbose_name='nom_collaborateur',max_length=30)
#     prenom_collaborateur = models.CharField(verbose_name='prenom_collaborateur', max_length=30)
#     representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)
#     nom_prenom_collaborateur = models.CharField(        verbose_name='nom_prenom_collaborateur',max_length=30)


# class Clients(models.Model):

#     representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)
#     denomination_client = models.CharField(verbose_name='denomination_client',max_length=30)
#     identifiant_national_client = models.CharField(verbose_name='identifiant_national_client',max_length=30)
#     type_identifiant_national_client = models.CharField(verbose_name='type_identifiant_national_client',max_length=30)

# class Affiliations(models.Model):
#     representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)
#     denomination_affiliation = models.CharField(verbose_name='denomination_affiliation',max_length=30)
#     identifiant_national_client = models.CharField(verbose_name='identifiant_national_client',max_length=30)
#     type_identifiant_national_client = models.CharField(verbose_name='type_identifiant_national_client',max_length=30)

# class Niveaux_intervention(models.Model):
#     niveau_intervention  = models.CharField(verbose_name='niveau_intervention',max_length=30)
#     representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)

# class Exercices(models.Model):
#      exercices_id = models.IntegerField(verbose_name='exercices_id', primary_key=True)
#      representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)
#      date_debut = models.CharField(verbose_name='date_debut',max_length=30)
#      date_fin = models.CharField(verbose_name='date_fin',max_length=30)
#      exercice_sans_activite = models.CharField(verbose_name='exercice_sans_activite',max_length=30)
#      nombre_activites = models.IntegerField(verbose_name='nombre_activites')
#      declaration_incomplete = models.CharField(verbose_name='declaration_incomplete',max_length=3)
#      date_publication = models.CharField(verbose_name='date_publication',max_length=30)
#      exercice_sans_CA = models.CharField(verbose_name='exercice_sans_CA',max_length=30)
#      montant_depense = models.CharField(verbose_name='montant_depense',max_length=30)
#      nombre_salaries = models.CharField(verbose_name='nombre_salaries',max_length=30)
#      chiffre_affaires = models.CharField(verbose_name='chiffre_affaires',max_length=30)
#      annee_debut = models.CharField(verbose_name='annee_debut',max_length=30)
#      annee_fin = models.CharField(verbose_name='annee_fin',max_length=30)
#      montant_depense_inf = models.CharField(verbose_name='montant_depense_inf',max_length=30)
#      montant_depense_sup = models.CharField(verbose_name='montant_depense_sup',max_length=30)
#      ca_inf = models.FloatField(verbose_name='ca_inf',max_length=30)
#      ca_sup = models.CharField(verbose_name='ca_sup',max_length=30)



class Objets_activites(models.Model):

    activite_id = models.IntegerField(        verbose_name='activite_id', primary_key=True)
    exercice_id = models.ForeignKey(Exercices, on_delete=models.CASCADE)
    date_publication_activite =  models.CharField(        verbose_name='date_publication_activite',max_length=30)
    identifiant_fiche = models.CharField(verbose_name='identifiant_fiche',max_length=30)
    objet_activite = models.CharField(verbose_name='objet_activite', max_length=30)
    


class Domaines_intervention(models.Model):

    domaineIntervention = models.CharField(        verbose_name='domaineIntervention', max_length=30)
    activite_id = models.ForeignKey(Objets_activites, on_delete=models.CASCADE)
    


class Observations(models.Model):

    action_representation_interet_id = models.IntegerField(        verbose_name='activite_id', primary_key=True)
    activite_id = models.ForeignKey(Objets_activites, on_delete=models.CASCADE)
    observation=models.CharField(        verbose_name='domaineIntervention', max_length=30)


class Decisions_concernees(models.Model):

    decision_concerne = models.IntegerField(      verbose_name='activite_id', primary_key=True)
    action_representation_interet_id = models.ForeignKey(Observations, on_delete=models.CASCADE)
   




class Beneficiaires(models.Model):  

    beneficiaire_action_menee = models.CharField(verbose_name='beneficiaire_action_menee', max_length=30)
    action_representation_interet_id = models.ForeignKey(Observations, on_delete=models.CASCADE)
    action_menee_en_propre = models.CharField(verbose_name='action_menee_en_propre',max_length=30)


class Actions_menees(models.Model):  

    action_menee = models.CharField(verbose_name='action_menee', max_length=30)
    action_representation_interet_id = models.ForeignKey(Observations, on_delete=models.CASCADE)
    action_menee_autre = models.CharField(verbose_name='action_menee_autre',max_length=30)


# class Secteur_activites(models.Model):  

#     secteur_activite = models.CharField(verbose_name='secteur_activite', max_length=30)
#     representants_id = models.ForeignKey(Informations_generales, on_delete=models.CASCADE)


class Ministeres_aai_api(models.Model):  

    action_representation_interet_id = models.ForeignKey(Observations, on_delete=models.CASCADE)
    responsable_public =  models.CharField(verbose_name='responsable_public',max_length=30)
    departement_ministeriel = models.CharField(verbose_name='departement_ministeriel',max_length=30)
    responsable_public_ou_dpt_ministeriel_autre = models.CharField(verbose_name='responsable_public_ou_dpt_ministeriel_autre',max_length=30)

def __str__(self):
    return self.ref
