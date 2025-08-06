from Calculates import rectangle, triangle, circle

w = int(input("What figure's area do you want to find? Write 1 if rectangle, 2 if triangle, 3 if circle: "))

if w == 1:
    a = int(input("Write the size of the side a: "))
    b = int(input("Write the size of the side b: "))
    print(f"Area rectangle", rectangle(a,b))
elif w == 2:
    h = int(input("Write the height 'h': "))
    a = int(input("Write the size of the side a: "))
    print(f"Area triangle", triangle(h, a))
elif w == 3:
    r = int(input("Write the radius 'r': "))
    print(f"Area circle", circle(r))
else:
    print("Wrong choice, there is no such figure.")