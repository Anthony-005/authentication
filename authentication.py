import hashlib

class PasswordSecurity:
    def check_strength(self, password: str) -> bool:
        if len(password) < 10:
            print(" Password is too short (minimum of 10 characters)!")
            return False
        if not any(char.isupper() for char in password):
            print(" Password must contain at least one uppercase letter!")
            return False
        if not any(char.islower() for char in password):
            print(" Password must contain at least one lowercase letter!")
            return False
        if not any(char.isdigit() for char in password):
            print(" Password must contain at least one number!")
            return False
        print(" Password strength validated.")
        return True

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()


class User:
    def __init__(self, username: str, hashed_password: str):
        self.username = username
        self.hashed_password = hashed_password
        self.failed_attempts = 0
        self.locked = False


class AuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> None:
        ps = PasswordSecurity()
        if ps.check_strength(password):
            hashed_pw = ps.hash_password(password)
            self.users[username] = User(username, hashed_pw)
            print(f"User '{username}' registered successfully.")
        else:
            print("Registration failed due to weak password.")

    def login(self, username: str, password: str) -> bool:
        if username not in self.users:
            print("Username not found.")
            return False

        user = self.users[username]

        if user.locked:
            print(f" Account '{username}' is locked due to multiple failed attempts.")
            return False

        ps = PasswordSecurity()
        hashed_input = ps.hash_password(password)

        if hashed_input == user.hashed_password:
            print(f" Login successful. Welcome, {username}!")
            user.failed_attempts = 0
            return True
        else:
            user.failed_attempts += 1
            print(" Incorrect password.")
            if user.failed_attempts >= 5:
                user.locked = True
                print(f" Account '{username}' has been locked after 5 failed attempts.")
            return False


# ---------------- INTERACTIVE DEMO ----------------
if __name__ == "__main__":
    system = AuthenticationSystem()

    print(" Welcome to the Authentication System")
    username = input("Enter a username to register: ")
    password = input("Enter a password: ")

    system.register(username, password)

    print("\n--- LOGIN ---")
    while True:
        login_user = input("Username: ")
        login_pass = input("Password: ")
        success = system.login(login_user, login_pass)
        if success:
            break
