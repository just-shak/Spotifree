#!/usr/bin/env python3

# installer flup et uwsgi pour utiliser les modules applicatifs pythons pour web
# lancer le script ./acceuil.fcgi
from flup.server.fcgi import WSGIServer
from main import app

if __name__ == "__main__":
    WSGIServer(
        app,
        bindAddress="/tmp/flaskr-fcgi.sock",
    ).run()
