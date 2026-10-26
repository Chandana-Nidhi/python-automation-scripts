import random
import string

def generate_password(length=12):
    """
    Generate a strong, secure random password containing
    letters, digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if _name_ == "_main_":
    print("--- Secure Password Generator ---")
    length = 12
    new_password = generate_password(length)
    print(f"Generated {length}-character password: {new_password}")
