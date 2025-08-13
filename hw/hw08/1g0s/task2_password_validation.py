def validate_password(password: str) -> tuple[bool, list[str]]:
    """
    Validates a password against security requirements.
    
    Args:
        password: The password to validate
        
    Returns:
        A tuple containing:
        - bool: True if password is valid, False otherwise
        - list[str]: List of error messages for failed validation rules
    """
    errors = []
    
    # Check length requirement (6-16 characters)
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
    elif len(password) > 16:
        errors.append("Password must be at most 16 characters long.")
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Must contain at least one lowercase letter.")
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Must contain at least one uppercase letter.")
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        errors.append("Must contain at least one digit.")
    
    # Check for at least one special character from [$#@]
    special_chars = "$#@"
    if not any(char in special_chars for char in password):
        errors.append("Must contain at least one special character from [$#@].")
    
    return len(errors) == 0, errors


def main():
    """Main function to run the password validation program."""
    print("Password Validation Program")
    print("=" * 30)
    
    password = input("Enter your password: ")
    
    is_valid, errors = validate_password(password)
    
    if is_valid:
        print("Valid password")
    else:
        print("Invalid password:")
        for error in errors:
            print(f"- {error}")


if __name__ == "__main__":
    main()