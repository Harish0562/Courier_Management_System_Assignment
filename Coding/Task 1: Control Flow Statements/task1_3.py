def authenticate_user(email, password, user_db):
    if email in user_db:
        if user_db[email] == password:
            return "Login successful!"
        else:
            return "Invalid password."
    else:
        return "User not found."

# Example usage
user_db = {
    "arjun@gmail.com": "password123",
    "kaviya@gmail.com": "securepass",
}

email = "arjun@gmail.com"
password = "password123"
print(authenticate_user(email, password, user_db))
