from PyPDF2 import PdfReader
from PIL import Image
import re
import pytesseract

# Chemin vers le fichier PDF
pdf_path = "C:/Users/21698/Desktop/sodapdf-converted.pdf"

# Fonction pour extraire le texte d'un PDF
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text
    

# Fonction pour extraire le texte d'une image en utilisant PyTesseract
def extract_text_from_image(image):
    return pytesseract.image_to_string(image, lang='ara')  # 'ara' pour la langue arabe

# Extraction du texte du PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Utilisation de PyTesseract pour extraire le texte d'une image (par exemple, en utilisant la première page du PDF)


print("Texte extrait du PDF :")
print(pdf_text)

pattern = re.compile(r'\b\d{8}\b')

matches= pattern.findall(pdf_text)
for i in matches :
    print (i)


