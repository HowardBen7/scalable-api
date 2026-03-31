def get_users():
    users = [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Doe", "email": "jane@example.com"}
    ]
    return users

def create_user(user_data):
    user = {
        "name": user_data.name,
        "email": user_data.email,
    }
    return user