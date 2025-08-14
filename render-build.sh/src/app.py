from flask import Flask, request, send_file, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from controllers.conversion_controller import ConversionController

app = Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['book']
    filename = secure_filename(uploaded_file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(file_path)

    controller = ConversionController()
    audio_file_path = controller.convert_file(file_path)

    if audio_file_path:
        audio_filename = os.path.basename(audio_file_path)
        return render_template('index.html', audio_file=audio_filename)
    else:
        return render_template('index.html', audio_file=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)