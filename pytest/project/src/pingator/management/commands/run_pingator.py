from django.core.management.base import BaseCommand
from pingator.models import Site, Log
import requests



class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        
        print "My site:"
        for site in Site.objects.filter(is_enabled=True):
            print "  parse:", site
            log = Log(site = site)            
            try:
                r = requests.get(site.url)
                log.is_ok = r.status_code == 200
                log.http_status = r.status_code                    
            except Exception, e:
                log.is_ok = False
                log.error_text = "%s" % e
            log.save()
            
        
  
