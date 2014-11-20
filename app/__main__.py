#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import argparse
from os.path import dirname, join as join_path
import sys

HERE = dirname(dirname(__file__))
sys.path.insert(0, HERE)

from app.wsgi import app


def command(options):
    app.run(debug=True)


def main(argv=sys.argv[1:]):
    try:
        arg_parser = argparse.ArgumentParser()

        options = arg_parser.parse_args(argv)
        command(options)
    except KeyboardInterrupt:
        pass

    return 0


if __name__ == '__main__':
    sys.exit(main())
