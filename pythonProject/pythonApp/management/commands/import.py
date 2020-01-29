from django.core.management.base import BaseCommand, CommandError
# from models import *
from pythonApp.models import * 
from django.db.models import * 
import csv
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

            Informations_generales.objects.all().delete()
            Dirigeants.objects.all().delete()

            info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']

Organization.objects.all().delete()
# Dirigeants.objects.all().delete()
info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']
class reader_test():
    with open("C:\Users\Mikazuki\Desktop\pythonProjectSeb\vueFusionnees\1_informations_generales.csv",encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader,None)
        for row in spamreader:
            obj = Organization()
            for tab in range(len(info_gen)):
                setattr(obj, info_gen[tab],row[tab])
            obj.save()
    print("--------------- Fin remplissage reader test ---------------")

import pandas as pd
data = pd.read_csv('C:\Users\Mikazuki\Desktop\pythonProjectSeb\vueFusionnees\1_informations_generales.csv')

for a in data: 
    representants_id = a:data[a]
    Organization.save(representants_id)
