from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bookmarks/', include('bookmarks.urls')),
    url(r'^admin/', include(admin.site.urls)),
)