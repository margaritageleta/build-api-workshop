import datetime
import string
import requests

from flask import Flask, jsonify, request, send_file, render_template
from flask_cors import CORS


# Setup Flask app.
flask_app = Flask(__name__)
flask_app.config['JSON_AS_ASCII'] = False  # Needed for proper UTF-8 support.

# Setup CORS - this is needed for a proper communication with the frontend.
CORS(flask_app)


@flask_app.route('/test', methods=['GET'])
def test():
    """
    This endpoint returns the current server time and a static text.
    :return: Current server time and text JSON formatted.
    """
    response = {
        'time': datetime.datetime.now().strftime('%m/%d/%Y - %H:%M:%S'),
        'text': 'This is a test.'
    }
    return jsonify(response), 200


@flask_app.route('/name', methods=['GET'])
def name():
    response = {
        'name': 'Rita'
    }
    return jsonify(response), 200

@flask_app.route('/calculator', methods=['GET'])
def calculator():
    val1 = request.args.get('val1', type = int)
    val2 = request.args.get('val2', type = int)
    response = {
        'result': val1 * val2
    }
    return jsonify(response), 200

@flask_app.route('/downloader', methods=['GET'])
def downloader():
    url = request.args.get('url', type = str)
    if url == None: ## No url, just /downloader
        response = {
            'error': True
        }
        return jsonify(response), 400
    image = requests.get(url, stream = True)
    with open ("src/imagen.jpeg", "wb") as file:
        file.write(image.content)
    response = {
        'url': url
    }
    return jsonify(response), 200


