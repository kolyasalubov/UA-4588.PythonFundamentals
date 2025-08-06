import re


def validate_pass(string: str):
    pass_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$")
    min_count = 6
    max_count = 16

    if pass_regex.fullmatch(string) is None:
        print("Password wasn't validated.")
        print("Please ensure you have:")
        if re.match('(?=.*[a-z])', string) is None:
            print(re.match('(?=.*[a-z])', string))
            print("- at least one letter between [a-z]")

        if re.match("(?=.*[A-Z])", string) is None:
            print("- at least one letter between [A-Z]")

        if re.match("(?=.*[0-9])", string) is None:
            print("- at least one number between [0-9]")

        if re.match("(?=.*[$#@])", string) is None:
            print("- at least one character from [$#@]")

        if min_count >= len(string) or len(string) >= max_count:
            print(f"- the length should be between {min_count} and {max_count} [including]")

        return False
    return True


if __name__ == "__main__":
    pass_accepted = False
    while not pass_accepted:
        user_password = input("Please, enter your password: ")

        if validate_pass(user_password):
            break

        if input("Do you want to continue?\n") == "":
            break

    print("Password was successfully validated.")