#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from flask import Flask

from .views import mod


class App(Flask):
    pass


app = App(__name__,
          template_folder='templates',
          static_folder='static')
app.register_blueprint(mod)
