PI = 3.14  # rounded and hardcoded PI const
figures = {
    "1": {
        "name": "Triangle",
        "elements": ["height", "base"],
        "function": lambda h, b: (h * b) / 2
    },
    "2": {
        "name": "Circle",
        "elements" : ["radius"],
        "function": lambda r: PI * r ** 2
    },
    "3": {
        "name": "Rectangle",
        "elements": ["A side", "B side"],
        "function": lambda a, b: a * b
    }
}


def triangle_area(h: float, b: float):
    """This function calculates the area of the triangle from base and height."""
    return (h * b) / 2


def rectangle_area(a: float, b: float):
    """This function calculates the area of the rectangle."""
    return a * b


def circle_area(r: float):
    """This function calculates the area of the circle."""
    return PI * r ** 2


def validate_input_value(help_string: str) -> float:
    console_value = input(help_string)

    for i in console_value.split("."):
        if not i.isdigit():
            print(
                "[error]: You should enter the valid number. Number must be greater than zero to calculate the correct area\n")
            return validate_input_value(help_string)
    return float(console_value)


print("This program calculates the area of the selected figure shape.\n")
while True:
    print("Please, choose the figure type:\n")
    for k, v in figures.items():
        print(f"{v.get("name")} - press {k}")
    print("\nTo exit the program just click ENTER button\n(Any other value is not accepted)\n")
    user_input = input("Enter the number: ")

    if not user_input:
        break

    figure_details = figures.get(user_input, None)

    if figure_details:
        elements = [validate_input_value(f"Enter the {i}: ") for i in figure_details.get("elements")]
        # Comment this if you don't want to use lambda functions
        area_function = figure_details.get("function")
        area = area_function(*elements)

        # !! Uncomment this to use the function call instead of lambda !!
        # area = 0
        # match user_input:
        #     case "1":
        #         area = triangle_area(*elements)
        #     case "2":
        #         area = circle_area(*elements)
        #     case "3":
        #         area = rectangle_area(*elements)

        print("*" * 10)
        print(f"The area of {figure_details.get("name")} is {area}")
        print("*" * 10)
    else:
        print(f"[error]: Please, enter the correct value\n\n")
