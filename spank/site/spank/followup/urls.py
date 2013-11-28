# -*- coding: UTF-8 -*-
# urls.py
#
# Copyright (C) 2013 HES-SO//HEG Arc
#
# Author(s): Cédric Gaspoz <cedric.gaspoz@he-arc.ch>
#
# This file is part of appagoo.
#
# appagoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# appagoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with appagoo.  If not, see <http://www.gnu.org/licenses/>.

# Stdlib imports

# Core Django imports
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Third-party app imports

# Appagoo imports
from . import views

urlpatterns = patterns('',
                       url(r'^result/(?P<number>\w+)/$', views.result, name='fup-result'),
                       url(r'^anonymize/(?P<player_id>\d+)/$', views.anonymize, name='fup-anonymize'),
                       url(r'^mailing/$', views.mailing, name='fup-mailing'),
                       url(r'^about$', TemplateView.as_view(template_name='followup/about.html'), name='fup-about'),
                       url(r'^profils', TemplateView.as_view(template_name='followup/profils.html'), name='fup-profils'),
                       url(r'^impressum$', TemplateView.as_view(template_name='followup/impressum.html'), name='fup-impressum'),
                       url(r'^contact$', TemplateView.as_view(template_name='followup/contact.html'), name='fup-contact'),
                       url(r'^$', views.index, name='fup-index'),
                       )
