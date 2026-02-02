# Data Extraction & Secure Validation

A Python program that reads raw text and extracts useful information like emails, URLs, phone numbers, hashtags, and credit cards.  
It validates the data and ignores anything invalid or unsafe, while masking sensitive details like email usernames and credit card numbers.  

The output is a clean, structured JSON file for easy use in other programs or analysis.

---

## What the program does

It can find and handle these types of data safely:

1. **Emails** – Detects standard emails, including ones with dots, underscores, plus signs, or subdomains. Invalid emails like `invalid@@example.com` are ignored.  
2. **URLs** – Detects web links starting with `http` or `https`. Unsafe links, like `javascript:` or `ftp://`, are ignored.  
3. **Phone Numbers** – Recognizes common formats like `(123) 456-7890`, `123-456-7890`, and `123.456.7890`. Invalid numbers are ignored.  
4. **Hashtags** – Finds hashtags that start with a letter and can include numbers or underscores. Hashtags with spaces are ignored.  
5. **Credit Cards** – Detects 16-digit credit cards with spaces or dashes. Only the last 4 digits are displayed to protect sensitive data.

---

## Safety Features

- **Email masking**: Only part of the username is shown (e.g., `jo***@example.com`)  
- **Credit card masking**: Only the last 4 digits appear (`**** **** **** 3456`)  
- **URL validation**: Unsafe links are rejected  
- **Phone validation**: Only 10-digit numbers are accepted  
- **Hashtag validation**: Invalid hashtags are ignored  

This keeps sensitive information safe.

---

## How to run the program

1. Clone the repository:

2. Go to the source folder:

3. Run the program:

4. The program reads `../samples/input.txt` and prints a **structured JSON output**.

---

## Sample Input (`input.txt`)


---

## Sample Output (`output.txt`)

```json
{
    "emails": [
        "jo***@example.com",
        "ja***@company.co.uk",
        "us***@subdomain.example.org"
    ],
    "urls": [
        "https://www.example.com"
    ],
    "phone_numbers": [
        "(123) 456-7890"
    ],
    "hashtags": [
        "#hello"
    ],
    "credit_cards": [
        "**** **** **** 3456"
    ]
}
