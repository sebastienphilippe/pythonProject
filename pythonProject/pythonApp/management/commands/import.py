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
        Dirigeants.objects.all().delete()
        Collaborateurs.objects.all().delete()
        Clients.objects.all().delete()
        Affiliations.objects.all().delete()
        Niveaux_intervention.objects.all().delete()
        Exercices.objects.all().delete()
        Objets_activites.objects.all().delete()
        Domaines_intervention.objects.all().delete()
        Observations.objects.all().delete()
        Decisions_concernees.objects.all().delete()
        Beneficiaires.objects.all().delete()
        Actions_menees.objects.all().delete()
        Secteur_activites.objects.all().delete()
        Ministeres_aai_api.objects.all().delete()

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

        dirigeants=['civilite_dirigeant','fonction_dirigeant','nom_dirigeant','prenom_dirigeant','representants_id','nom_prenom_dirigeant']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/2_Dirigeants.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Dirigeants()
                for tab in range(len(dirigeants)):
                    setattr(obj, dirigeants[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        collaborateurs=['civilite_collaborateur','fonction_collaborateur','nom_collaborateur','prenom_collaborateur','representants_id','nom_prenom_collaborateur']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/3_Collaborateurs.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Collaborateurs()
                for tab in range(len(collaborateurs)):
                    setattr(obj, collaborateurs[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

         clients=['representants_id','denomination_client','identifiant_national_client','type_identifiant_national_client']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/4_Clients.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Clients()
                for tab in range(len(clients)):
                    setattr(obj, clients[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        affiliations=['representants_id','denomination_affiliation','identifiant_national_affiliation','type_identifiant_national_affiliation']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/5_Affiliations.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Affiliations()
                for tab in range(len(affiliations)):
                    setattr(obj, affiliations[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        niveaux_intervention=['niveau_intervention','representants_id']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/6_Niveaux_intervention.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Niveaux_intervention()
                for tab in range(len(niveaux_intervention)):
                    setattr(obj, niveaux_intervention[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        exercices=['exercices_id','representants_id','date_debut','date_fin','exercice_sans_activite','nombre_activites','declaration_incomplete','date_publication','exercice_sans_CA','montant_depense','nombre_salaries','chiffre_affaires','annee_debut','annee_fin','montant_depense_inf','montant_depense_sup','ca_inf','ca_sup']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/7_Exercices.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Exercices()
                for tab in range(len(exercices)):
                    setattr(obj, exercices[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        objets_activites=['activite_id','exercices_id','date_publication_activite','identifiant_fiche','objet_activite']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/8_Objets_activites.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Objets_activites()
                for tab in range(len(objets_activites)):
                    setattr(obj, objets_activites[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        domaines_intervention=['domaines_intervention_actions_menees','activite_id']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/9_Domaines_intervention.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Domaines_intervention()
                for tab in range(len(domaines_intervention)):
                    setattr(obj, domaines_intervention[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        observations=['action_representation_interet_id','activite_id','observation']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/10_Observations.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Observations()
                for tab in range(len(observations)):
                    setattr(obj, observations[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        decisions_concernees=['decision_concernee','action_representation_interet_id']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/11_Decisions_concernees.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Decisions_concernees()
                for tab in range(len(decisions_concernees)):
                    setattr(obj, decisions_concernees[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        benef=['beneficiaire_action_menee','action_representation_interet_id','action_menee_en_propre']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/12_Beneficiaires.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Beneficiaires()
                for tab in range(len(info_gen)):
                    setattr(obj, info_gen[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        actions_menees=['action_menee','action_representation_interet_id','action_menee_autre']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/13_Actions_menees.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Actions_menees()
                for tab in range(len(actions_menees)):
                    setattr(obj, actions_menees[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        secteur_activites=['secteur_activite','representants_id']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/14_Secteur_activites.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Secteur_activites()
                for tab in range(len(secteur_activites)):
                    setattr(obj, secteur_activites[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        ministeres_aai_api=['action_representation_interet_id','responsable_public','departement_ministeriel','responsable_public_ou_dpt_ministeriel_autre']
        with open("C:/Users/Sebastien/pythonProject/pythonProject/vueFusionnees/15_Ministeres_aai_api.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Ministeres_aai_api()
                for tab in range(len(ministeres_aai_api)):
                    setattr(obj, ministeres_aai_api[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")

        
        # Organization.objects.all().delete()
