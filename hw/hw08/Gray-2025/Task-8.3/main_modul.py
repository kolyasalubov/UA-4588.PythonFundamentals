import calculator

print("Оберіть фігуру, площу якої треба розрахувати:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Круг")

choice = int(input("Введіть номер фігури: "))

if choice == 1:
    a = float(input("Введіть довжину прямокутника: "))
    b = float(input("Введіть ширину прямокутника: "))
    result = round(calculator.area_of_rectangle(a, b), 2)

elif choice == 2:
    c = float(input("Введіть довжину однієї строни трикутника: "))
    h = float(input("Введіть висоту трикутника, опущену на відповідну сторону: "))
    result = round(calculator.area_of_triangle(c, h), 2)

elif choice == 3:
    r = float(input("Введіть радіус кола: "))
    result = round(calculator.area_of_circle(r), 2)

else:
    print("Ви зробили некоректрий вибір! Повторіть спробу ще раз.")

print("Площа обраної вами фігури становить", result, "од.кв..")