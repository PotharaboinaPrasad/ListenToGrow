from werkzeug.utils import secure_filename
import os

def save_uploaded_file(uploaded_file, upload_folder):
    filename = secure_filename(uploaded_file.filename)
    file_path = os.path.join(upload_folder, filename)
    uploaded_file.save(file_path)
    return file_path

def generate_audio_filename(original_filename):
    return os.path.splitext(original_filename)[0] + '.mp3'