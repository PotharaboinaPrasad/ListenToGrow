import os
from services.pdf_extractor import extract_text_from_pdf
from services.image_extractor import extract_text_from_image
from services.tts_service import text_to_speech

class ConversionController:
    def convert_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        text = None

        if ext == '.pdf':
            text = extract_text_from_pdf(file_path)
        elif ext in ['.jpg', '.jpeg', '.png']:
            text = extract_text_from_image(file_path)
        else:
            return None

        if not text or not text.strip():
            return None

        audio_file_path = os.path.splitext(file_path)[0] + '.mp3'
        text_to_speech(text, audio_file_path)
        return audio_file_path