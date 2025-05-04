Polymorphism plays a vital role in OOPS concepts. Based on the different scenario, same entity behaves in different forms. 

## **Class Polymorphism**
Different class have same method name which behaves based on the object type. In the below example, Car and Auto are the two different classes having same method name `number_of_wheels`. Based on the object type, the same function gives the different result in output

    #Class Polymorphism
    class Car:
        def number_of_wheels(self):
            print("I have four wheels")
            
    class Auto:
        def number_of_wheels(self):
            print("I have three wheels")

    #Number of wheels function behaves based on the object type
    for vehicle in (Car(), Auto()):
        vehicle.number_of_wheels()

 Output

    I have four wheels
    I have three wheels


## **Function Polymorphism**
Same function which behaves differently for different scenario called as function polymorphism. Below is the simple example in python for function polymorphism

    #Function polymorphism
    input_list = [10, 20, 30, 40 ,50]
    input_string = "Rathna Schools"
    input_dict = { 1:"python", 2:"Java", 3:"Javascript" }

    #Calling the len function
    print(len(input_list))
    print(len(input_string))
    print(len(input_dict))

 Output

    5
    14
    3


## **Operator Overloading**
In python, operator overloading can be achieved like the below example. '+' operator behaves differently for the different input data types

    #Operator Overloading
    # '+' operator perform addition operation for numbers
    num1 = 10
    num2 = 20
    print(num1+num2)

    # '+' operator perform concatenation for strings
    word1 = "Rathna "
    word2 = "Schools"
    print(word1+word2)


## **Method Overriding**
Overriding the parent method definition in their child class is called as method overriding. Below is the simple example for method overriding in python.

    class Shape:
        def draw(self):
            pass

    class Square(Shape):
        def draw(self):
            print("I am drawing a square")
            
    class Circle(Shape):
        def draw(self):
            print("I am drawing a circle")

    #Similar to class polymorphism but here child class methods override the parent method
    for shape in (Square(), Circle()):
        shape.draw()

 Output

    I am drawing a square
    I am drawing a circle

## **Method Overloading**
In other programming language, we can achieve method overloading by calling the method with different number of arguments. But, its impossible in python which always consider the last definition of the method.

    class Shape:
        def draw(self):
            pass

    class Circle(Shape):
        def draw(self):
            print("I am drawing a circe")

        def draw(self, radius):
            print("I am drawing a circle with {}cm".format(radius))
        
    circle = Circle()
    #This method works without any issues
    circle.draw(10)

    #Raises Exception, since second(last) draw method overrides the first(previous) method
    circle.draw()

 Output

    I am drawing a circle with 10cm
    Traceback (most recent call last):
    File "<string>", line 16, in <module>
    TypeError: draw() missing 1 required positional argument: 'radius'