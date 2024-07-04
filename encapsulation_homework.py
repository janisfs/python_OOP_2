class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    # Getter methods
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level

class Admin(User):
    def __init__(self, user_id, name):
        # Вызов конструктора родительского класса User
        super().__init__(user_id, name, access_level='admin')
        self.__users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
        else:
            print("Invalid user")

    def remove_user(self, user_id):
        self.__users = [user for user in self.__users if user.get_user_id() != user_id]

    def get_users(self):
        return self.__users

# Пример использования классов
# Создание экземпляров класса User
user1 = User(1, "Анна")
user2 = User(2, "Борис")
user3 = User(3, "Света")

# Создание экземпляра класса Admin
admin = Admin(4, "Катя")

# Добавление пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Удаление пользователя
admin.remove_user(1)

# Вывод списка пользователей
for user in admin.get_users():
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Вывод информации об администраторе
print(f"Admin ID: {admin.get_user_id()}, Name: {admin.get_name()}, Access Level: {admin.get_access_level()}")
