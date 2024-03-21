import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Authenticate user with email and password
def authenticate_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # User exists, authenticate with provided password
        auth.get_user_by_email_and_password(email, password)
        return True
    except auth.UserNotFoundError:
        # User not found
        return False
    except auth.AuthError:
        # Invalid email or password
        return False

# Example usage
if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if authenticate_user(email, password):
        print("Authentication successful!")
    else:
        print("Authentication failed.")
