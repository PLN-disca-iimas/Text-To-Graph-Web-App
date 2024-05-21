from flask import send_from_directory, send_file
import os

from src import app
from src.constants import ROOT_ABSOLUTE_PATH




@app.route('/assets/<filename>/', methods=['GET'])
def assets_manager(filename):

    return send_from_directory(os.path.join(ROOT_ABSOLUTE_PATH, 'src', 'static'), filename.replace("&","/"))

@app.route('/download-file/<filename>/', methods=['GET'])
def download_asset(filename):

    return send_file(os.path.join(ROOT_ABSOLUTE_PATH, 'src', 'static', filename.replace("&","/")), as_attachment=True)