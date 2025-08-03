import figur_area

figure = int(input('1 - Rectangle \n2 - Triangle \n3 - Circle \n Select the figure: '))

if figure == 1:
    a = int(input('Input a value: '))
    b = int(input('Input b value: '))
    print("Are of a rectangle is:",int(figur_area.rectangle_area(a,b)))
elif figure == 2:
    a = int(input('Input a value: '))
    h = int(input('Input h value: '))
    print("Are of a tringale is:", int(figur_area.triangle_area(a,h)))
elif figure == 3:
    r = int(input('Input r value: '))
    print("Are of a circle is:", int(figur_area.circle_area(r)))
else:
    print("Chose the correct option")