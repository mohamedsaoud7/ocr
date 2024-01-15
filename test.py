import re

pattern1 = re.compile(r'\b[2579]\d{7}\b')
filePath = "dummyData.txt"
with open(filePath, 'r', encoding='utf-8') as file:
    textContent = file.read()
# print(textContent)
# extractedDummyPhoneNumbers = pattern1.findall(textContent)
# print(extractedDummyPhoneNumbers)
# age_pattern = re.compile(r'\b(\d{1,2})\s*سنة\b', re.IGNORECASE)
# ages = age_pattern.findall(textContent)
# print(ages)
    # skills_pattern = re.compile(r"المهارات: (.+)")
    # matchedSkills = skills_pattern.search(textContent)
    # skills = []
    # if matchedSkills:
    #     skills = matchedSkills.group(1).split(', ')
    # date_pattern = r"\d{2}/\d{2}/\d{4}"
    # dates = re.findall(date_pattern, textContent)
    # years = [int(date.split("/")[-1]) for date in dates]
    # experience = 0
    # if(years):
    #     experience = max(years) - min(years)
    # keywords_pattern = words_pattern = r'(حسنت|صممت|زدت|أرباح)' 
    # keywords = re.findall(words_pattern, textContent)
    # print(experience)
    # print(keywords)
    # print(skills)
    policy_number_pattern = r"رقم البوليصة: (\d+)"
    matchedPolicy_number = re.search(policy_number_pattern, textContent)
    policy_number = -1
    if matchedPolicy_number:
        policy_number = matchedPolicy_number.group(1)
    insured_party_pattern = r"المؤمن عليه: (.+)"
    matchedInsured_party = re.search(insured_party_pattern, textContent)
    insured_party = ""
    if matchedInsured_party:
        insured_party = matchedInsured_party.group(1)
    coverage_details_pattern = r"التغطية: (.+)"
    matchedCoverage_details = re.search(coverage_details_pattern, textContent)
    coverage_details = ""
    if matchedCoverage_details:
        coverage_details = matchedCoverage_details.group(1)
    premium_amount_pattern = r"قسط التأمين: (\d+(\.\d+)?)"
    matchedPremium_amount = re.search(premium_amount_pattern, textContent)
    premium_amount = -1
    if matchedPremium_amount:
        premium_amount = matchedPremium_amount.group(1)
print("Policy Number:", policy_number)
print("Insured Party:", insured_party)
print("Coverage Details:", coverage_details)
print("Premium Amount:", premium_amount)
