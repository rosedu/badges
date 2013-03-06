#!/usr/bin/env python

import os
import flask
from flask.ext.script import Manager


def create_app():
    app = flask.Flask(__name__)
    app.debug = (os.environ.get('DEBUG') == 'on')
    return app


manager = Manager(create_app)

if os.environ.get('RELOAD') != 'on':
    manager._commands['runserver'].use_reloader = False


if __name__ == '__main__':
    manager.run()
