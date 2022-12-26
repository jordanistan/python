# Create your own Audiobook or convert any pdf to audio format with this killer automation script that uses Text-to-speech and PyPDF2 module. 
# This is handy when you want to convert your whole PDF book or Text to audio format.

# PDF to Audio
# pip install text-to-speech
# pip install PyPDF2
from text_to_speech import speak
from PyPDF2 import PdfFileReader
def PDFtoAudio(pdf_path):
    text = []
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        for page in pdf.pages:
            text.append(page.extractText())
    speak(' '.join(text), 'en', save=True, file='audio_book.mp3')
PDFtoAudio('demo.pdf')