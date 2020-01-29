from django.core.management.base import BaseCommand, CommandError
# from models import *
from pythonApp.models import * 
from django.db.models import * 
import csv

# Dirigeants_2=['civilite_dirigeant','fonction_dirigeant','nom_dirigeant','prenom_dirigeant','representants_id','nom_prenom_dirigeant']
# Collaborateurs_3=['civilite_collaborateur','fonction_collaborateur','nom_collaborateur','prenom_collaborateur','representants_id','nom_prenom_collaborateur']
# Clients_4=['representants_id','denomination_client','identifiant_national_client','type_identifiant_national_client']
# affiliation=['representants_id','denomination_affiliation','identifiant_national_affiliation','type_identifiant_national_affiliation']
# niveau_intervention=['niveau_intervention','representants_id']
# exercice=['exercices_id','representants_id','date_debut','date_fin','exercice_sans_activite','nombre_activites','declaration_incomplete','date_publication','exercice_sans_CA','montant_depense','nombre_salaries','chiffre_affaires','annee_debut','annee_fin','montant_depense_inf','montant_depense_sup','ca_inf','ca_sup']
# object_activite=['activite_id','exercices_id','date_publication_activite','identifiant_fiche','objet_activite']
# domaine_intervention=['domaines_intervention_actions_menees','activite_id']
# observation=['action_representation_interet_id','activite_id','observation']
# decision_concerne=['decision_concernee','action_representation_interet_id']
# benef=['beneficiaire_action_menee','action_representation_interet_id','action_menee_en_propre']
# action_menee=['action_menee','action_representation_interet_id','action_menee_autre']
# sect_act=['secteur_activite','representants_id']
# minister_ai=['action_representation_interet_id','responsable_public','departement_ministeriel','responsable_public_ou_dpt_ministeriel_autre']

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        Informations_generales.objects.all().delete()
        # Dirigeants.objects.all().delete()
        # Collaborateurs.objects.all().delete()
        # Clients.objects.all().delete()
        # Affiliations.objects.all().delete()
        # NiveauxIntervention.objects.all().delete()
        # Exercices.objects.all().delete()
        # objetActivite.objects.all().delete()
        # domaineIntervention.objects.all().delete()
        # observation.objects.all().delete()
        # decision_concerne.objects.all().delete()
        # benef.objects.all().delete()
        # action_menee.objects.all().delete()
        # sect_act.objects.all().delete()
        # minister_ai.objects.all().delete()


        info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/1_Informations_generales.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Informations_generales()
                for tab in range(len(info_gen)):
                    setattr(obj, info_gen[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")
        # Organization.objects.all().delete()
