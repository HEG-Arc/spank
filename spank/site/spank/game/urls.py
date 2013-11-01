from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from game import views

urlpatterns = patterns('',

    # ex: /game/autorisations
    url(r'^permissions/$', TemplateView.as_view(template_name='game/permissions.html'), name='permissions'),

    url(r'^refused/$', TemplateView.as_view(template_name='game/refused.html'), name='refused'),

    url(r'^page1$', views.page1),
    url(r'^page2$', TemplateView.as_view(template_name='game/2.html'), name='page2'),
    url(r'^page3$', TemplateView.as_view(template_name='game/3.html'), name='page3'),
    url(r'^page4$', TemplateView.as_view(template_name='game/4.html'), name='page4'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<number_id>\d+)/$', views.edit, name='edit'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^page7$', TemplateView.as_view(template_name='game/7.html'), name='page7'),
    url(r'^page8$', TemplateView.as_view(template_name='game/8.html'), name='page8'),
    url(r'^page9$', TemplateView.as_view(template_name='game/9.html'), name='page9'),
    url(r'^page10$', TemplateView.as_view(template_name='game/10.html'), name='page10'),
    url(r'^page11$', TemplateView.as_view(template_name='game/11.html'), name='page11'),
    url(r'^page12$', TemplateView.as_view(template_name='game/12.html'), name='page12'),
    url(r'^page13$', TemplateView.as_view(template_name='game/13.html'), name='page13'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^process/$', TemplateView.as_view(template_name='game/process.html'), name='process'),
    url(r'^page18$', TemplateView.as_view(template_name='game/18.html'), name='page18'),
    url(r'^roulette/$', TemplateView.as_view(template_name='game/roulette.html'), name='roulette'),
    url(r'^multiply/(?P<factor_id>\d+)/$', views.multiply, name='multiply'),
    url(r'^bye/$', views.bye, name='bye'),
    url(r'^qrcode/$', TemplateView.as_view(template_name='game/qrcode.html'), name='qrcode'),
)