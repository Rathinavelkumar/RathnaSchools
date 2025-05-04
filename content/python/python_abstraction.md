Abstraction helps to abstract or hide the internal logic of a function from the end user. User knows "what the function does" but no idea on "how it does".
It reduces the overall application complexity and enhance application security. The abc module in python helps to achieve the abstraction in the program

## **Abstract Class**
Below is an example for abstraction which is implemented with the help of abstract classes and methods

    #Abstract class
    from abc import ABC, abstractmethod

    class Shapes(ABC):
        @abstractmethod
        def number_of_sides():
            pass

    class Square(Shapes):
        def number_of_sides(self):
            print("Square - Four Sides")
            
    class Triangle(Shapes):
        def number_of_sides(self):
            print("Triangle - Three Sides")
            
    class Pentagon(Shapes):
        def number_of_sides(self):
            print("Pentagon - Five Sides")

    square = Square()
    square.number_of_sides()

    triangle = Triangle()
    triangle.number_of_sides()

    pentagon = Pentagon()
    pentagon.number_of_sides()

 Output

    Square - Four Sides
    Triangle - Three Sides
    Pentagon - Five Sides

## **Abstract Methods**
Shaped(ABC) forces the child class to implement its abstract method.
    
    #Abstract Method
    from abc import ABC, abstractmethod

    class Shapes(ABC):
        @abstractmethod
        def number_of_sides():
            pass

    class Circle(Shapes):
        def print_shape(self):
            print("I am circle")

    circle = Circle()
    circle.print_shape()

Output:

    Traceback (most recent call last):
    File "<string>", line 13, in <module>
    TypeError: Can't instantiate abstract class Circle with abstract methods number_of_sides

To overcome this error, abstract methods helps to avoid the compulsory implementation

    #Abstract Methods
    from abc import ABC, abstractmethod

    #ABC - NotInherited
    class Shapes():
        @abstractmethod
        def number_of_sides():
            pass

    class Circle(Shapes):
        def print_shape(self):
            print("I am circle")

    circle = Circle()
    circle.print_shape()

 Output

    I am circle