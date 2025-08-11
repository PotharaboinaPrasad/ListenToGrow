# Audiobook Backend

This project is a backend application that converts uploaded books (PDFs and images) into audiobooks, making them ready for playback. It utilizes Flask for the web framework, PyPDF2 for PDF text extraction, Pillow and pytesseract for image text extraction, and gTTS for text-to-speech conversion.

## Project Structure

```
audiobook-backend
├── src
│   ├── app.py                     # Entry point of the application
│   ├── controllers
│   │   └── conversion_controller.py # Handles file conversion requests
│   ├── services
│   │   ├── pdf_extractor.py        # Extracts text from PDF files
│   │   ├── image_extractor.py      # Extracts text from image files
│   │   └── tts_service.py          # Converts text to speech
│   ├── utils
│   │   └── file_utils.py           # Utility functions for file operations
│   └── types
│       └── __init__.py             # Custom types and interfaces
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd audiobook-backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```
   python src/app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

3. **Upload a PDF or image file:**
   Use the provided form to upload a book file. The application will process the file and return an audio version.

## Dependencies

- Flask
- PyPDF2
- Pillow
- pytesseract
- gTTS

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.