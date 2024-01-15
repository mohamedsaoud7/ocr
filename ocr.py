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
selected_domain = st.selectbox("Select the domain for data extraction:", ['التسويق', 'تؤمين'])

st.title("Extraction de données depuis un PDF")
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

    

    cin_pattern = re.compile(r'\b[01]\d{7}\b')
    cin= cin_pattern.findall(pdf_text)
    num_tel_pattern = re.compile(r'\b[2579]\d{7}\b')
    num_tel=num_tel_pattern.findall(pdf_text)
    nouns_pattern = re.compile("|".join(map(re.escape, liste_de_noms)), re.IGNORECASE)
    nouns= nouns_pattern.findall(pdf_text)
    region_pattern = re.compile("|".join(map(re.escape, liste_de_regions)), re.IGNORECASE)
    regions= region_pattern.findall(pdf_text)
    age_pattern = re.compile(r'\b(\d{1,2})\s*سنة\b', re.IGNORECASE)
    ages = age_pattern.findall(pdf_text)

    claim_number_pattern = r"رقم المطالبة: (\d+)"
    matchedClaim_number = re.search(claim_number_pattern, pdf_text)
    claim_number = ""
    if matchedClaim_number:
        claim_number = matchedClaim_number.group(1)
    claim_date_pattern = r"تاريخ المطالبة: (\d{2}/\d{2}/\d{4})"
    claim_date = ""
    matchedClaim_date = re.search(claim_date_pattern, pdf_text)
    if matchedClaim_date:
        claim_date = matchedClaim_date.group(1)
    claim_type_pattern = r"نوع المطالبة: (.+)"
    claim_type = ""
    matchedClaim_type = re.search(claim_type_pattern, pdf_text)
    if matchedClaim_type:
        claim_type = matchedClaim_type.group(1)
    claim_amount_pattern = r"قيمة المطالبة: (\d+(\.\d+)?)"
    claim_amount = ""
    matchedClaim_amount = re.search(claim_amount_pattern, pdf_text)
    if matchedClaim_amount:
        claim_amount = matchedClaim_amount.group(1)
    
    if selected_domain == 'التسويق':
        st.subheader("رقم بطاقة التعريف")
        st.write(cin)
        
        st.subheader("الاسماء")
        st.write(nouns)

        st.subheader("الاماكن")
        st.write(regions)

        st.subheader("رقم الهاتف")
        st.write(num_tel)

        st.subheader("الأعمار")
        st.write(ages)

    elif selected_domain == 'تؤمين':
        st.subheader("رقم المطالبة")
        st.write(claim_number)

        st.subheader("تاريخ المطالبة")
        st.write(claim_date)

        st.subheader("نوع المطالبة")
        st.write(claim_type)

        st.subheader("قيمة المطالبة")
        st.write(claim_amount)







