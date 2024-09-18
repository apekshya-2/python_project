def print_validation_result(is_valid,data_type):
    if is_valid:
        print(f"{data_type}is valid")
    else:
        print(f"{data_type} is invalid")

def print_error_message(message):
    print(f"error:{message}")