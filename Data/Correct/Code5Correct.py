# Correct Code
# filename: Code5Correct.py

class Backend:
    def __init__(self, database):
        self.database = database

    def get_user(self, user_id):
        return self.database.get(user_id)

    def create_user(self, user_id, user_data):
        if user_id in self.database:
            raise ValueError("User already exists")
        self.database[user_id] = user_data

    def update_user(self, user_id, user_data):
        if user_id not in self.database:
            raise ValueError("User does not exist")
        self.database[user_id] = user_data

    def delete_user(self, user_id):
        if user_id not in self.database:
            raise ValueError("User does not exist")
        del self.database[user_id]
        
    def list_users(self):
        return list(self.database.keys())

    def authenticate_user(self, user_id, password):
        user = self.get_user(user_id)
        if user and user.get('password') == password:
            return True
        return False

    def change_password(self, user_id, old_password, new_password):
        user = self.get_user(user_id)
        if user and user.get('password') == old_password:
            user['password'] = new_password
        else:
            raise ValueError("Old password is incorrect")

    def search_users(self, query):
        return {user_id: data for user_id, data in self.database.items() if query.lower() in user_id.lower() or query.lower() in str(data).lower()}

    def get_user_profile(self, user_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        return {
            "user_id": user_id,
            "profile": user.get('profile', {})
        }

    def update_user_profile(self, user_id, profile_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        user['profile'] = profile_data

    def deactivate_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        user['active'] = False

    def activate_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        user['active'] = True

    def get_active_users(self):
        return {user_id: data for user_id, data in self.database.items() if data.get('active', True)}

    def get_inactive_users(self):
        return {user_id: data for user_id, data in self.database.items() if not data.get('active', True)}