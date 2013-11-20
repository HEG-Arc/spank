from django.conf.urls import patterns, url, include
from game import views
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^spank/', TemplateView.as_view(template_name='game/intro.html'), name='intro'),
    url(r'^game/', include('game.urls')),
    url(r'^booth/', include('booth.urls')),
    url(r'^qr/', include('qrcodegen.urls')),
    url(r'^f/', include('followup.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)