import datetime

class User:
    def __init__(self, login, first_name, last_name, age):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.registration_date = datetime.datetime.now()  # Записуємо поточну дату при створенні об'єкту

    def display_user_info(self):
        print("Логін:", self.login)
        print("Ім'я:", self.first_name)
        print("Прізвище:", self.last_name)
        print("Вік:", self.age)
        print("Дата заповнення анкети:", self.registration_date.strftime("%Y-%m-%d %H:%M:%S"))

# Створюємо екземпляр класу User з інформацією про користувача
user = User(login="user123", first_name="Андрій", last_name="Алексейчук", age=18)

# Виводимо інформацію про користувача на екран
user.display_user_info()
