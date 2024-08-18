## The args argument lets you input any number of arguments which will be passed in tuple form 

def add(*args):
    output = 0
    for n in args:
        output += n

    return output


## The **kwargs argument is an optional paramter indicator. 
# It creates a dictionary with keys and value elements created from the arguments used whne calling the function. 

def add_then_multiply(n, **kwargs):
    n+= kwargs["add_num"]
    n*= kwargs["mul_num"]
    
    return n


class Car():
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make")  
        self.model = kwargs.get("model")
        self.color = kwargs.get("color") #We use the .get function so that None is returned if the argument is not included when the function is called.


# print(add(1, 4, 6, 12, 3, 2))

# print(add_then_multiply(2, add_num = 2, mul_num = 4))

car_1 = Car(make="Toyota", model="Camry")
print(car_1.make)
print(car_1.model)
print(car_1.color)


