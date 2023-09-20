class Employee:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def calculate_salary(self, position, experience):
        # Визначаємо оклад в залежності від посади та стажу
        salary = 0
        if position == "Менеджер":
            salary = 30000 + 1000 * experience
        elif position == "Розробник":
            salary = 40000 + 1500 * experience
        elif position == "Тестувальник":
            salary = 35000 + 1200 * experience

        # Розраховуємо податковий збір (припустимо 18%)
        tax = 0.18 * salary

        return salary, tax

# Створюємо екземпляр класу Employee і ініціалізуємо прізвище та ім'я співробітника
employee = Employee(last_name="Алексейчук", first_name="Андрій")

# Розраховуємо оклад та податковий збір для співробітника з певною посадою та стажем
position = "Розробник"
experience = 3

salary, tax = employee.calculate_salary(position, experience)

# Виводимо інформацію про співробітника, оклад та податковий збір
print(f"Прізвище: {employee.last_name}")
print(f"Ім'я: {employee.first_name}")
print(f"Посада: {position}")
print(f"Оклад: {salary} гривень")
print(f"Податковий збір: {tax} гривень")
