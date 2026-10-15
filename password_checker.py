
import getpass
import string


COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "iloveyou"
}


def check_password(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Check character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Consider adding symbols.")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("Avoid common passwords.")

    # Assign a rating
    if password.lower() in COMMON_PASSWORDS or len(password) < 8:
        rating = "Weak"
    elif score >= 6 and len(password) >= 12:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback


def main():
    print("=== PASSWORD STRENGTH CHECKER ===")
    print("Enter a test password to check its strength.")
    print("Do not enter your real account password.\n")

    password = getpass.getpass("Enter password: ")

    if not password:
        print("Password cannot be empty.")
        return

    rating, feedback = check_password(password)

    print("\nPassword strength:", rating)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("No basic improvements suggested by these checks.")

    print("\nNote: This is a basic educational checker,")
    print("not a guarantee that a password is secure.")


if __name__ == "__main__":
    main()
