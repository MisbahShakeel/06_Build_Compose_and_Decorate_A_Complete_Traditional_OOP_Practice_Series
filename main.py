# 1. Using self

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Alice", 85)
s1.display()

# 2. Using cls


class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total instances created: {cls.count}")

c1 = Counter()
c2 = Counter()
Counter.display_count()


# 3. Public Variables and Methods

class Car():
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

class ElectricCar(Car):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

    def start(self):
        print(f"{self.brand} with {self.battery_capacity} kWh battery is starting silently.")

c1 = Car("Toyota")
c1.start()

c2 = ElectricCar("Tesla", 100)
c2.start()


#  4. Class Variables and Class Methods

class Bank():
    bank_name = "Global Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

b1 = Bank()
b1.change_bank_name("HBL Bank")
print(f"Bank Name: {b1.bank_name}")


# 5. Static Variables and Static Methods

class MathUtils():
    @staticmethod
    def add(a, b):
        return a + b

result_add = MathUtils.add(5, 10)
print(f"Addition Result: {result_add}")


# 6. Constructors and Destructors

class logger():
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

l = logger()
del l  # This will call the destructor and print the message.


# 7. Access Modifiers: Public, Private, and Protected

class Employee():
    def __init__(self, name, salary):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = 1000         # Private variable

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")


#  8. The super() Function

class Animal():
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"{self.sound} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Bark")
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, sound: {self.sound}")

    def make_sound(self):
        print(f"{self.name} barks.")

d = Dog("Buddy", "Golden Retriever")
d.display_info()
d.make_sound()

# 9. Abstract Classes and Methods

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")   

d = Dog()
d.make_sound()
c = Cat()
c.make_sound()

# 10. Instance Methods

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Buddy", "Golden Retriever")
d.bark()

# 11. Class Methods

class Book():
    total_books = 0

    def increament_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
b1 = Book()
b1.increament_book_count()  

# 12. Static Methods

class TemperatureConverter():
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")


# 13. Composition

class Engine():
    def start(self):
        print("Engine started.")

class Car():
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start_car()

# 14. Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_details(self):
        print(f"Department: {self.dept_name}, Employee: {self.employee.name}")

emp = Employee("John Doe")
dept = Department("HR", emp)
dept.show_details()

# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        print("show from class A")
class B(A):
    def show(self):
        print("show from class B")

class C(A):
    def show(self):
        print("show from class C")
class D(B, C):
    def show(self):
        print("show from class D")
d = D()
d.show()

# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage:
p = Product(100)
print(p.price)      # Get price
p.price = 150       # Set price
print(p.price)
del p.price         # Delete price

# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiplier(3)
print(callable(m))       
print(m(10))       

# 20. Creating a Custom Exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Age is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

# 21. Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Example usage:
for num in Countdown(5):
    print(num)