import math
def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

print("Вибиріть фігуру для обчислення площі:")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Коло")

choice = input("Ваш вибір (1/2/3): " )

if choice == "1":
    l = float(input("Ведіть довжину: "))
    w = float(input("Ведіть ширину: "))
    print(f"Площа прямокутника: {rectangle_area(l, w):.2f}")

elif choice =="2":
    b = float(input("Ведіть основу: "))
    h = float(input("Ведіть висоту: "))
    print(f"Площа трикутника: {triangle_area(b, h):.2f}")

elif choice =="3":
    r = float(input("Ведіть радіус: "))
    print(f"Площа кола: {circle_area(r):.2f}")

else:
    print("Невірний вибір! Спробуй ще раз.")