from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from game import views

urlpatterns = patterns('',

    url(r'^welcome/$', TemplateView.as_view(template_name='game/welcome.html'), name='welcome'),

    # ex: /game/autorisations
    url(r'^permissions/$', views.permissions, name='permissions'),

    url(r'^refused/$', TemplateView.as_view(template_name='game/refused.html'), name='refused'),

    url(r'^intro$', TemplateView.as_view(template_name='game/intro.html'), name='intro'),
    url(r'^page1$', views.page1, name='page1'),
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
    url(r'^question1$', views.question1, name='question1'),
    url(r'^page12$', views.page12, name='page12'),
    url(r'^question2$', views.question2, name='question2'),
    url(r'^page13$', views.page13, name='page13'),
    url(r'^question3$', views.question3, name='question3'),
    url(r'^page14$', views.page14, name='page14'),
    url(r'^page15$', TemplateView.as_view(template_name='game/15.html'), name='page15'),
    url(r'^page16$', TemplateView.as_view(template_name='game/16.html'), name='page16'),
    url(r'^chart$', views.chart, name='chart'),
    url(r'^privacy1$', views.privacy1, name='privacy1'),
    url(r'^privacy2$', views.privacy2, name='privacy2'),
    url(r'^interesting/$', TemplateView.as_view(template_name='game/interesting.html'), name='interesting'),
    url(r'^access/$', TemplateView.as_view(template_name='game/access.html'), name='access'),
    url(r'^process/$', TemplateView.as_view(template_name='game/process.html'), name='process'),
    url(r'^page18$', TemplateView.as_view(template_name='game/18.html'), name='page18'),
    url(r'^roulette/$', TemplateView.as_view(template_name='game/roulette.html'), name='roulette'),
    url(r'^multiply/(?P<factor_id>\d+)/$', views.multiply, name='multiply'),
    url(r'^bye/$', views.bye, name='bye'),
    url(r'^qrcode/$', TemplateView.as_view(template_name='game/qrcode.html'), name='qrcode'),

    url(r'^gipc/$', TemplateView.as_view(template_name='game/gipc.html'), name='gipc'),
    url(r'^gipcq/(?P<sequence>\d+)/$', views.gipc_question, name='gipc_question'),

    url(r'^page17$', TemplateView.as_view(template_name='game/17.html'), name='page17'),
    url(r'^page19$', TemplateView.as_view(template_name='game/19.html'), name='page19'),
    url(r'^page20$', TemplateView.as_view(template_name='game/20.html'), name='page20'),
    url(r'^page21$', TemplateView.as_view(template_name='game/21.html'), name='page21'),
    url(r'^chart2$', views.chart2, name='chart2'),
    url(r'^page22$', TemplateView.as_view(template_name='game/22.html'), name='page22'),
    url(r'^culprit/(?P<name>\w+)/$', views.coupable, name='culprit'),
    url(r'^culprit/$', views.coupable, name='culprit'),
    url(r'^page24/(?P<accept>\w+)/$', views.page24, name='page24'),
)