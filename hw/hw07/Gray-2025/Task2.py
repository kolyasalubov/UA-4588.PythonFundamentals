# Напишіть програму, яка обчислює площу прямокутника, трикутника та кола
# (напишіть три функції для обчислення площі. І викликайте їх у головній програмі
# залежно від вибору користувача).

def area_of_rectangle(a, b):
    '''
    Calculate the area of a rectangle.
    '''
    return a * b

def area_of_triangle(c, h):
    '''
    Calculate the area of a triangle.
    '''
    return 0.5 * c * h

def area_of_circle(d):
    '''
    Calculate the area of a circle
    '''
    return 3.14 * (d / 2) ** 2

print("Оберіть фігуру, площу якої треба розрахувати:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Круг")

choice = int(input("Введіть номер фігури: "))

if choice == 1:
    a = float(input("Введіть довжину прямокутника: "))
    b = float(input("Введіть ширину прямокутника: "))
    result = round(area_of_rectangle(a, b), 2)

elif choice == 2:
    c = float(input("Введіть довжину однієї строни трикутника: "))
    h = float(input("Введіть висоту трикутника, опущену на відповідну сторону: "))
    result = round(area_of_triangle(c, h), 2)

elif choice == 3:
    d = float(input("Введіть діаметр кола: "))
    result = round(area_of_circle(d), 2)

else:
    print("Ви зробили некоректрий вибір! Повторіть спробу ще раз.")

print("Площа обраної вами фігури становить", result, "од.кв..")