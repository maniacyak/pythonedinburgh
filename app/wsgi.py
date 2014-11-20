#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from flask import Flask, render_template

from .views import mod


class App(Flask):
    pass

app = App("pythonedinburgh",
          template_folder='templates',
          static_folder='static')
app.register_blueprint(mod)
