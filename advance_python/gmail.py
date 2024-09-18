email = input("Enter your email: ")  # Example: g@g.in

k, j, d = 0, 0, 0  # Flags to track different errors

if len(email) >= 6:  # Condition 1: Length should be at least 6 characters
    if email[0].isalpha():  # Condition 2: First character should be alphabetic
        if "@" in email and email.count("@") == 1:  # Condition 3: Only one "@" symbol
            if email[-4] == "." or email[-3] == ".":  # Condition 4: "." at the right place
                for i in email:
                    if i.isspace():  # Condition 5a: Check for spaces
                        k = 1
                    elif i.isalpha():
                        if i.isupper():  # Condition 5b: Uppercase letters are not allowed
                            j = 1
                    elif i.isdigit():
                        continue  # Digits are allowed
                    elif i == "_" or i == "." or i == "@":  # These special characters are allowed
                        continue
                    else:
                        d = 1  # Any other character is invalid
                
                # After loop finishes, check if any flags were triggered
                if k == 1:
                    print("Invalid email: contains spaces.")
                elif j == 1:
                    print("Invalid email: contains uppercase letters.")
                elif d == 1:
                    print("Invalid email: contains invalid characters.")
                else:
                    print("Valid Email")
            else:
                print("Invalid email: '.' not at the correct position.")  # Condition 4 failed
        else:
            print("Invalid email: '@' symbol issue.")  # Condition 3 failed
    else:
        print("Invalid email: First character is not alphabetic.")  # Condition 2 failed
else:
    print("Invalid email: Too short.")  # Condition 1 failed
