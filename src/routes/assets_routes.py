from flask import send_from_directory, send_file
import os

from src import app
from dotenv import load_dotenv

load_dotenv()



@app.route('/assets/<filename>/', methods=['GET'])
def assets_manager(filename):
    """
    Route handler for serving static assets.

    Args:
        filename (str): The name of the file to be served.

    Returns:
        Response: The file specified by the filename parameter.

    Raises:
        NotFound: If the file specified by the filename parameter does not exist.

    """
    return send_from_directory(os.path.join(os.getenv("ROOT_ABSOLUTE_PATH", "/"), 'src', 'static'), filename.replace("&","/"))

@app.route('/download-file/<filename>/', methods=['GET'])
def download_asset(filename):
    """
    Download the specified asset file.

    Args:
        filename (str): The name of the file to be downloaded.

    Returns:
        Response: The file to be downloaded as an attachment.
    """
    return send_file(os.path.join(os.getenv("ROOT_ABSOLUTE_PATH", "/"), 'src', 'static', filename.replace("&","/")), as_attachment=True)