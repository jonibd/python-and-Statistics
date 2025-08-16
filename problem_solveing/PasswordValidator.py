def is_valid_password(password):
    special_chars = "!@#$%^&*"
    
    if len(password) < 8:
        return False

    has_upper = has_lower = has_digit = has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

passwrd=input("Enter your passward :")
s= is_valid_password(passwrd)
print(s)
