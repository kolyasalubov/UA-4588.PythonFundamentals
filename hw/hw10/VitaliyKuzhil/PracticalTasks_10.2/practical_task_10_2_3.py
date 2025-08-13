def God():
    return [Man(), Woman()]


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


god = God()
print(god[0].__class__, god[1].__class__)
