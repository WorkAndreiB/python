import secrets
import string


def generate_password(length=12):
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    password = generate_password(int(input("Enter the desired password length: ")))
    print("Generated password:", password)

if __name__ == "__main__":
    main()