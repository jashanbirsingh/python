def is_valid_password(password):
    # Check if the password is at least five characters long
    if len(password) < 5:
        return False

    # Check if the password contains the symbol "&"
    if '&' not in password:
        return False

    # Check if the password contains at least one uppercase and one lowercase letter
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if not (has_upper and has_lower):
        return False

    return True

def main():
    while True:
        password = input("Enter a password: ")

        if is_valid_password(password):
            print("Password set successfully!")
            break
        else:
            print("Invalid password. Please try again.")

if __name__ == "__main__":
    main()
