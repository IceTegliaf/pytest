from django.db import models
import datetime



class Site(models.Model):
    url = models.URLField()
    is_enabled = models.BooleanField(default=True)
     
    def __unicode__(self):
        return "%s: %s" % (self.id, self.url)
         
class Log(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    site = models.ForeignKey(Site)
    is_ok = models.BooleanField()
    http_status = models.PositiveIntegerField(null=True)
    error_text = models.TextField()
    
    cool = 3 
    