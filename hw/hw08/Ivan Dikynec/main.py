from math import pi, pow
import areas

print("Виберіть фігуру для обчислення: ")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Коло")

choice = input("Ваш вибір (1/2/3): ")

if choice == "1":
    a = float(input("Введіть довжину: "))
    b = float(input("Введіть ширину: "))
    print(f"Площа прямокутника: {areas.rectangel_area(a, b):.2f}")
elif choice == "2":
    h = float(input("Введіть висоту: "))
    a = float(input("Введіть основу: "))
    print(f"Площа трикутнику: {areas.triangel_area(h, a):.2f}")
elif choice =="3":
    r = float(input("Введіть радіус: "))
    print(f"Площа кола: {areas.circle_area(r, pi, pow):.2f}")
else:
    print("Невірний вибір! Спробуй ще раз.")