import re
import json

# Step 1: Read raw text
with open("../samples/input.txt", "r") as f:
    raw_text = f.read()

# Step 2: Define regular expressions patterns.
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
url_pattern = r"\bhttps?:\/\/[^\s]+"
phone_pattern = r"(?:\(\d{3}\)\s*|\d{3}[\s.-]?)\d{3}[\s.-]?\d{4}"


hashtag_pattern = r"#\w+"
credit_card_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"

# Step 3: Extract matches
emails = re.findall(email_pattern, raw_text)
urls = re.findall(url_pattern, raw_text)
phones = re.findall(phone_pattern, raw_text)
hashtags = re.findall(hashtag_pattern, raw_text)
credit_cards_raw = re.findall(credit_card_pattern, raw_text)

# Step 4: Security and validation
def mask_email(email):
    username, domain = email.split("@")
    masked = username[:2] + "***" if len(username) > 2 else username[0] + "*"
    return masked + "@" + domain

emails = [mask_email(e) for e in emails]

urls = [u for u in urls if not u.lower().startswith("javascript:")]

def valid_phone(p):
    digits = re.sub(r"\D", "", p)
    return len(digits) == 10

phones = [p for p in phones if valid_phone(p)]
hashtags = [h for h in hashtags if " " not in h]

def mask_credit_card(card):
    digits = re.sub(r"\D", "", card)
    return "**** **** **** " + digits[-4:] if len(digits) == 16 else None

credit_cards = [mask_credit_card(c) for c in credit_cards_raw if mask_credit_card(c)]

# Step 5: Prepare well stuctured output 
output = {
    "emails": emails,
    "urls": urls,
    "phone_numbers": phones,
    "hashtags": hashtags,
    "credit_cards": credit_cards
}

# Step 6: Print JSON output
print(json.dumps(output, indent=4))
