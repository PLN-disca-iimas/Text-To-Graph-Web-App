from flask import Flask

app = Flask("Text To Graph Web App", template_folder="src/templates/", static_url_path='', 
            static_folder='src/static',)