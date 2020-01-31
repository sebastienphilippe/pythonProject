from django.core.management.base import BaseCommand, CommandError
# from models import *
from pythonApp.models import * 
from django.db.models import * 
import csv

class Command(BaseCommand):
   

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
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\1_Informations_generales.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Informations_generales()
                for tab in range(len(info_gen)):
                    setattr(obj, info_gen[tab],row[tab])
                obj.save()
        print("--------------- Fin remplissage reader test ---------------")
       
        
        Dirigeants_2=['civilite_dirigeant','fonction_dirigeant','nom_dirigeant','prenom_dirigeant','representants_id','nom_prenom_dirigeant']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\2_Dirigeants.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Dirigeants()
                for tab in range(len(Dirigeants_2)):
                    if(Dirigeants_2[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj, Dirigeants_2[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        Clients_4=['representants_id','denomination_client','identifiant_national_client','type_identifiant_national_client']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\4_Clients.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Clients()
                for tab in range(len(Clients_4)):
                    if(Clients_4[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj, Clients_4[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        Collaborateurs_3=['civilite_collaborateur','fonction_collaborateur','nom_collaborateur','prenom_collaborateur','representants_id','nom_prenom_collaborateur']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\3_Collaborateurs.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Collaborateurs()
                for tab in range(len(Collaborateurs_3)):
                    if(Collaborateurs_3[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj, Collaborateurs_3[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        affiliation=['representants_id','denomination_affiliation','identifiant_national_affiliation','type_identifiant_national_affiliation']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\5_Affiliations.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Affiliations()
                for tab in range(len(affiliation)):
                    if(affiliation[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj,affiliation[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        niveau_intervention=['niveau_intervention','representants_id']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\6_Niveaux_intervention.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Niveaux_intervention()
                for tab in range(len(niveau_intervention)):
                    if(niveau_intervention[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj,niveau_intervention[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        exercice=['exercices_id','representants_id','date_debut','date_fin','exercice_sans_activite','nombre_activites','declaration_incomplete','date_publication','exercice_sans_CA','montant_depense','nombre_salaries','chiffre_affaires','annee_debut','annee_fin','montant_depense_inf','montant_depense_sup','ca_inf','ca_sup']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\7_Exercices.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Exercices()
                for tab in range(len(exercice)):
                    if(exercice[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj,exercice[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        object_activite=['activite_id','exercices_id','date_publication_activite','identifiant_fiche','objet_activite']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\8_Objets_activites.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Objets_activites()
                for tab in range(len(object_activite)):
                    if(object_activite[tab] == 'exercices_id'):
                        row[tab] = Exercices.objects.get(exercices_id=row[tab])
                    setattr(obj,object_activite[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        domaine_intervention=['domaines_intervention_actions_menees','activite_id']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\9_Domaines_intervention.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Domaines_intervention()
                for tab in range(len(domaine_intervention)):
                    if(domaine_intervention[tab] == 'activite_id'):
                        row[tab] = Objets_activites.objects.get(activite_id = row[tab])
                    setattr(obj,domaine_intervention[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        observation=['action_representation_interet_id','activite_id','observation']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\10_Observations.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Observations()
                for tab in range(len(observation)):
                    if(observation[tab] == 'activite_id'):
                        row[tab] = Objets_activites.objects.get(activite_id = row[tab])
                    setattr(obj,observation[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        decision_concerne=['decisions_concernees','action_representation_interet_id']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\11_Decisions_concernees.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Decisions_concernees()
                for tab in range(len(decision_concerne)):
                    if(decision_concerne[tab] == 'action_representation_interet_id'):
                        row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                    setattr(obj,decision_concerne[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        benef=['beneficiaire_action_menee','action_representation_interet_id','action_menee_en_propre']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\12_Beneficiaires.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Beneficiaires()
                for tab in range(len(benef)):
                    if(benef[tab] == 'action_representation_interet_id'):
                        row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                    setattr(obj,benef[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")

        action_menee=['action_menee','action_representation_interet_id','action_menee_autre']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\13_Actions_menees.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Actions_menees()
                for tab in range(len(action_menee)):
                    if(action_menee[tab] == 'action_representation_interet_id'):
                        row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                    setattr(obj,action_menee[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")


        sect_act=['secteur_activite','representants_id']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\14_Secteur_activites.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Secteur_activites()
                for tab in range(len(sect_act)):
                    if(sect_act[tab] == 'representants_id'):
                       row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                    setattr(obj, sect_act[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")


        minister_ai=['action_representation_interet_id','responsable_public','departement_ministeriel','responsable_public_ou_dpt_ministeriel_autre']
        with open("C:\\Users\\THIAW-THI\\Desktop\\pythonProject\\pythonProject\\vueFusionnees\\15_Ministeres_aai_api.csv",encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Ministeres_aai_api()
                for tab in range(len(minister_ai)):
                    if(minister_ai[tab] == 'action_representation_interet_id'):
                        row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                    setattr(obj,minister_ai[tab],row[tab])
                obj.save()  
        print("--------------- Fin remplissage reader test ---------------")



