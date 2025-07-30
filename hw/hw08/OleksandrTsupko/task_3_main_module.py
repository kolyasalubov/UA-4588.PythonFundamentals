import task_3_functions_for_calculating_area as calc_area


shape_choosing = int(input("Please select a shape to calculate its area:\n \
Push '1' button for calculating area of a rectangle\n \
Push '2' button for calculating area of a triangle\n \
Push '3' button for calculating area of a circle\n"))

match shape_choosing:
    case 1:
        calc_area.calculating_area_of_rectangle()
    case 2:
        calc_area.calculating_area_of_triangle()
    case 3:
        calc_area.calculating_area_of_circle()
    case _:
        print("Wrong input!")