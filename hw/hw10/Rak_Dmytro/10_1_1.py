class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(sides=4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# 🔹 Приклад використання
rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())  # ➤ 15

# Запитуємо у користувача ввести довжину та ширину
try:
    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))

    # Створюємо об'єкт класу Rectangle
    rect = Rectangle(length, width)

    # Виводимо площу прямокутника
    print(f"Площа прямокутника: {rect.area()}")

except ValueError:
    print("Будь ласка, введіть дійсні числа.")
