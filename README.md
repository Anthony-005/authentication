#🔐 Authentication System

## 📌 Project Overview
This project implements a simple authentication system in Python. It demonstrates password strength validation, secure password hashing, user registration, and login with account lockout after repeated failed attempts. The goal is to highlight core cybersecurity concepts such as authentication, password policies, hashing, and access control.

---

## ✨ Features
- **Password Strength Validation**:
  - Minimum length: 10 characters
  - Must include at least one uppercase letter
  - Must include at least one lowercase letter
  - Must include at least one number
- **Password Hashing**: Uses SHA‑256 to securely store passwords.
- **User Registration**: Creates new accounts with validated passwords.
- **Login Authentication**: Compares hashed input against stored hash.
- **Account Lockout**: Locks account after 3 failed login attempts.

---

## 🛠 System Design
The system is structured into three main classes:

- **PasswordSecurity** → Validates password rules and hashes passwords.  
- **User** → Represents a registered user with username, hashed password, failed attempts, and lockout status.  
- **AuthenticationSystem** → Manages registration, login, and lockout logic.  

---

## 🚀 How to Run
1. Save the code as `authentication.py`.
2. Open a terminal and navigate to the project folder:
   ```bash
   cd "C:\Users\Admin\Downloads\gmail\authentication"
