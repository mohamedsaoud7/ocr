import re

pattern1 = re.compile(r'\b[2579]\d{7}\b')
filePath = "dummyData.txt"
extracted_data = {}
liste_de_noms = ["محمد", "ياسين", "حسام", "احمد","شاهين","اميمة","اشرف","منال","اية","تسنيم","مريم","حسان"]
liste_de_regions =["تونس","اريانة","سوسة","بن عروس","قبلي","تطاوين","جندوبة","صفاقص","منستير"]

with open(filePath, 'r', encoding='utf-8') as file:
    textContent = file.read()
    selected_fields =  ["رقم بطاقة التعريف", "الاسماء", "الاماكن", "رقم الهاتف"]
    
    if "رقم بطاقة التعريف" in selected_fields:
        pattern0 = re.compile(r'\b[01]\d{7}\b')
        cin = pattern0.findall(textContent)
        extracted_data["رقم بطاقة التعريف"] = cin

    if "الاسماء" in selected_fields:
        patter2 = re.compile("|".join(map(re.escape, liste_de_noms)), re.IGNORECASE)
        nouns = patter2.findall(textContent)
        extracted_data["الاسماء"] = nouns

    if "الاماكن" in selected_fields:
        patter3 = re.compile("|".join(map(re.escape, liste_de_regions)), re.IGNORECASE)
        regions = patter3.findall(textContent)
        extracted_data["الاماكن"] = regions

    if "رقم الهاتف" in selected_fields:
        pattern1 = re.compile(r'\b[2579]\d{7}\b')
        num_tel = pattern1.findall(textContent)
        extracted_data["رقم الهاتف"] = num_tel

print(extracted_data["رقم بطاقة التعريف"])
print(extracted_data["الاسماء"])
print(extracted_data["الاماكن"])
print(extracted_data["رقم الهاتف"])
