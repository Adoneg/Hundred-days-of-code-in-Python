def calculate(n, **kwargs):  # **kwargs is called unlimited key word argument.
    n += kwargs["subtract"]
    n *= kwargs["sum"]
    print(kwargs)


calculate(2, subtract=3, sum=5, divide=8)


class Car:
    def __init__(self, **kw):  # **kw can be used to initialise several keyword argument
        self.color = kw["color"]  # here, if u don't pass in a value(argument) for color,
        # u will get a keyword error
        self.move = kw.get("move")  # whereas the get function return none if a value(argument) if not passed in
        self.run = kw.get("run")
        self.mark = kw.get("mark")


my_car = Car(move="fast", color="Blue")
# my_car["move"] = ""

print(my_car.move)
