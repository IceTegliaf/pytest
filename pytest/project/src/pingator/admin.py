from django.contrib import admin
from pingator.models import Site, Log

class SiteAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "is_enabled" )
    list_filter = ("is_enabled",)
    list_editable = ("url", "is_enabled" )
    search_fields = ("url",)

admin.site.register(Site, SiteAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ("id", "when", "site", "is_ok", "http_status", "error_text")
    list_filter = ("is_ok",)
       

admin.site.register(Log, LogAdmin)
