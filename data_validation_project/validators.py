# validators.py

import re

def validate_email(email):
    # Regex for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_pattern, email))

def validate_age(age):
    try:
        age = int(age)
        if 18 <= age <= 99:
            return True
        return False
    except ValueError:
        return False

def validate_phone(phone_number):
    if phone_number.isdigit() and len(phone_number) == 10:
        return True
    return False

def validate_name(name):
    return name.isalpha()
