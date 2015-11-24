# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG or True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes = True)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
                            (r'^(?P<path>favicon\.ico)$', 'django.views.static.serve', {'document_root' : os.path.join(settings.STATIC_ROOT, "i")})
                        )
