from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls.static import static
from casjenkinsstats import settings
from casjenkinsstatsapp import adminView, mainView

urlpatterns = patterns('',
    url(regex=r'^admin', view=adminView.initPage, name='casjenkinsstatsapp.mainView.main'),
    url(regex='^$', view=mainView.initPage, name='casjenkinsstatsapp.adminView.main'),

    # url(regex=r'^tests', view=views.buildsTests, name='casjenkinsstatsapp.views.main'),

    # Examples:
    # url(r'^$', 'casjenkinsstats.views.home', name='home'),
    # url(r'^casjenkinsstats/', include('casjenkinsstats.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
