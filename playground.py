# defining arguments to get the sum of all outputs when calling function called (unlimited positional arguments)
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5))


# kwargs makes the outputs into a dictionary
def calculate(n, **kwargs):
    # adding n to add number then multiplying with multiply number in output
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

# creating a class using kwargs
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
