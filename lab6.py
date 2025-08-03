import re
import emoji
from datetime import datetime

def clean_text(text):
    pattern= r'[#$%^&*?>.!@]'
    text= re.sub(pattern, '', text)
    return text

# Example usage
input_text = "This is a #sample text! Remove the #hashtag and noise! Visit @example?"
output_text = clean_text(input_text)
print(output_text)


def remove_emojis(text):
    return emoji.replace_emoji(text, '')

def normalize_text(text):
    return ' '.join(text.lower().split())

def extract_dates(text):
    date_patterns = [
        r'\b(\d{2})/(\d{2})/(\d{4})\b',  # DD/MM/YYYY
        r'\b(\d{2})-(\d{2})-(\d{4})\b',  # MM-DD-YYYY
        r'\b((?: January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'  # Month Day, Year
    ]
    dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        if matches:
            dates.append(matches)
    return dates

def extract_phone_numbers(text):
    phone_patterns = [
        r'\b \d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        r'\+\(\d{1,2}\)\- \d{10}',
        r'\b(\(\d{1,2}\) \d{10})\b',
        ]
    matches = []
    standardized_numbers=[]
    for pattern in phone_patterns:
        match= re.findall(pattern, text)
        if match:
            matches.extend(match)
            
    for num in matches:
        cleaned_num= re.sub(r'\D', '', num)
        if len(cleaned_num)==10:
            standardized_numbers.append(f"{cleaned_num[:3]}-{cleaned_num[3:6]}- {cleaned_num[6:]}")
        else:
            extra_digits= len(cleaned_num)-10
            if extra_digits==1:
                standardized_numbers.append(f"+({cleaned_num[0]}) {cleaned_num[1:4]}-{cleaned_num[4:7]}- {cleaned_num[7:]}")
            else:
                standardized_numbers.append(f"+({cleaned_num[:2]}) {cleaned_num[2:5]}-{cleaned_num[5:8]}- {cleaned_num[8:]}")
    return standardized_numbers, matches





# Example usage
input_text = "This is a #sample text! Remove the #hashtag and noise! Visit @example. Call me at 123 456-7890 or 987-654-3210 or +(91)- 8888855555. Meet me on 12/05/2023 or June 15, 2024 😊."
dates_extracted = extract_dates(input_text)
input_text = remove_emojis(input_text)
input_text = normalize_text(input_text)
phone_numbers_extracted, matches = extract_phone_numbers(input_text)

print("Cleaned Text:", input_text)
print("Extracted Dates:", dates_extracted)
print("Extracted Phone Numbers:", phone_numbers_extracted, matches)
