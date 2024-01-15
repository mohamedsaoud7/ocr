import PyPDF2
from PIL import Image
import re
import streamlit as st
import pdfplumber
from bidi.algorithm import get_display


# Fonction pour extraire le texte d'un PDF
def extraire_texte_pdf(chemin_pdf):
    texte = ""
    try:
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                texte += get_display(page.extract_text())
    except Exception as e:
        st.error(f"Erreur lors de l'ouverture du fichier PDF : {e}")
    return texte

liste_de_noms = ["محمد", "ياسين", "حسام", "احمد","شاهين","اميمة","اشرف","منال","اية","تسنيم","مريم","حسان"]
liste_de_regions =["تونس","اريانة","سوسة","بن عروس","قبلي","تطاوين","جندوبة","صفاقص","منستير"]


'''**************************************************************************************'''
st.title("Extraction de données depuis un PDF avec Streamlit")
pdf_path = st.file_uploader("Sélectionnez un fichier PDF", type="pdf")
print(pdf_path)

if pdf_path is not None:

    # Extraction du texte du PDF
    pdf_text = extraire_texte_pdf(pdf_path)
    print(pdf_text)
    

    # Utilisation de PyTesseract pour extraire le texte d'une image (par exemple, en utilisant la première page du PDF)
    # Affichage du texte extrait
    st.subheader("Texte extrait du PDF:")
    st.text(pdf_text)

    

    pattern0 = re.compile(r'\b[01]\d{7}\b')
    cin= pattern0.findall(pdf_text)
    pattern1 = re.compile(r'\b[2579]\d{7}\b')
    num_tel=pattern1.findall(pdf_text)

    patter2 = re.compile("|".join(map(re.escape, liste_de_noms)), re.IGNORECASE)
    nouns= patter2.findall(pdf_text)
    patter3 = re.compile("|".join(map(re.escape, liste_de_regions)), re.IGNORECASE)
    regions= patter3.findall(pdf_text)

    st.subheader("رقم بطاقة التعريف")
    st.write(cin)
    
    st.subheader("الاسماء")
    st.write(nouns)

    st.subheader("الاماكن")
    st.write(regions)

    st.subheader("رقم الهاتف")
    st.write(num_tel)








