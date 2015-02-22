from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_sinhumo.views.home', name='home'),
    url(r'^denunciar$', 'app_sinhumo.views.denunciar', name='denunciar'),
    url(r'^legislacion$', 'app_sinhumo.views.legislacion', name='legislacion'),
    url(r'^quienes_somos$', 'app_sinhumo.views.quienes_somos', name='quienes_somos'),
    url(r'^como_funciona$', 'app_sinhumo.views.como_funciona', name='como_funciona'),
    url(r'^contacto$', 'app_sinhumo.views.contacto', name='contacto'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
