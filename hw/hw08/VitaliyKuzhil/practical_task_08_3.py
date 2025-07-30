import area_task_08_3 as area_module
import math

user_choice = int(input('What do you want to calculate?\n 1 - rectangle, 2 - triangle, 3 - circle? '))

match user_choice:
    case 1:
        len_rectangle = float(input('Enter length of a rectangle: '))
        width_rectangle = float(input('Enter width of a rectangle: '))
        
        rectangle = area_module.area_of_rectangle(len_reg = len_rectangle, width_reg = width_rectangle)
        print(f'The area of the rectangle is: {rectangle}')

    case 2:
        base_triangle = float(input('Enter base of a triangle: '))
        height_triangle = float(input('Enter height of a triangle: '))

        triangle = area_module.area_of_triangle(base_tri = base_triangle, height_tri = height_triangle)
        print(f'The area of the triangle is: {triangle}')

    case 3:
        radius_circle = float(input('Enter radius of a circle: '))
        
        circle = area_module.area_of_circle(radius_circle)
        print(f'The area of the circle is: {round(circle, 5)} or {circle / math.pi}')

    case _:
        print('You must choice one of tre three choices. Try again!')