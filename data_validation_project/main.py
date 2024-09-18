from validators import validate_email, validate_age, validate_phone, validate_name
from utils import print_validation_result, print_error_message

def main():
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    phone_number = input("Enter your phone number: ")
    name = input("Enter your name: ")

    # Validate email
    is_email_valid = validate_email(email)
    print_validation_result(is_email_valid, "email")

    # Validate age
    is_age_valid = validate_age(age)
    print_validation_result(is_age_valid, "age")

    # Validate phone number
    is_phone_valid = validate_phone(phone_number)
    print_validation_result(is_phone_valid, "phone number")

    # Validate name
    is_name_valid = validate_name(name)
    print_validation_result(is_name_valid, "name")

# Corrected __name__ == "__main__" block
if __name__ == "__main__":
    main()
