# -*- coding: UTF-8 -*-
# views.py
#
# Copyright (C) 2013 Degustare
#
# Author(s): Cédric Gaspoz <cga@degustare.ch>
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
from base64 import b64encode
import cStringIO

# Core Django imports
from django.http import HttpResponse
from django.template.base import Library

# Third-party app imports
import qrcode

# Degustare imports

register = Library()


def create_png(request, player_id):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(player_id)
    qr.make(fit=True)
    qr_image = qr.make_image()
    response = HttpResponse(mimetype="image/png")
    qr_image.save(response, "PNG")
    return response