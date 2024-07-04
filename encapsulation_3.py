class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"User(ID: {self.__id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print("Error: Invalid user object.")

    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_id() == user_id:
                self.__user_list.remove(user)
                print(f"User with ID {user_id} removed successfully.")
                return
        print(f"Error: User with ID {user_id} not found.")

    def get_user_list(self):
        return [str(user) for user in self.__user_list]

    def get_access_level(self):
        return self.__access_level


# Пример использования
if __name__ == "__main__":
    # Создание обычного пользователя
    user1 = User(1, "Alice")
    print(user1)

    # Создание администратора
    admin = Admin(100, "Bob")
    print(admin)

    # Добавление пользователей администратором
    admin.add_user(user1)
    admin.add_user(User(2, "Charlie"))

    # Вывод списка пользователей
    print("\nUser list:")
    for user in admin.get_user_list():
        print(user)

    # Удаление пользователя
    admin.remove_user(1)

    # Вывод обновленного списка пользователей
    print("\nUpdated user list:")
    for user in admin.get_user_list():
        print(user)