import random
import string

def generate_password(length, use_numbers, use_uppercase, use_lowercase, use_special):
    # Define the character sets based on user preferences
    characters = ''
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_special:
        characters += string.punctuation

    # Ensure at least one character set is selected
    if not characters:
        raise ValueError("At least one character set must be selected")

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        # Ask the user for the length of the password
        length = int(input("Enter the length of the password: "))
        
        # Ask the user if they want to include specific types of characters
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate the password
        password = generate_password(length, use_numbers, use_uppercase, use_lowercase, use_special)
        
        # Print the generated password
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()