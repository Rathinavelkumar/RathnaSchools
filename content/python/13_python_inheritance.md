Inheritance is one of the powerful feature in OOPS. Through which we can inherit the properties from another class, so that the code can be reused without written of same code again and again

## **Types of Inheritance**
OOPS is a very famous and popular programming paradigm

* **`Single Inheritance`** 
* **`Multiple Inheritance`**
* **`Multilevel Inheritance`**
* **`Hierarchical Inheritance`**
* **`Hybrid Inheritance`**

## **Single Inheritance**
In single inheritance, child class inherits from only one parent class. By calling the parent class name in child class, single inheritance can be implemented easily in python

    #Parent class
    class Fruit:
        def fruits_benefits(self):
            print("I am parent class : Fruits Benefits")

    #Child class    
    class Apple(Fruit):
        def apple_benefits(self):
            print("I am child class : Apple Benefits")

    #Object creation
    apple_fruit = Apple()
    #Access the parent method
    apple_fruit.fruits_benefits()
    #Access the child method
    apple_fruit.apple_benefits()

 Output

    I am parent class : Fruits Benefits
    I am child class : Apple Benefits

## **Multiple Inheritance**
In multiple inheritance, child class inherits from only more than one parent class. By calling the multiple parent class name in child class, multiple inheritance can be implemented

    #Parent class - 1
    class Fruit:
        def fruits_benefits(self):
            print("I am parent class 1 : Fruits Benefits")
            
    #Parent class - 2
    class Flower:
        def flower_benefits(self):
            print("I am parent class 2 : Flower Benefits")
            
    #Child class    
    class Apple(Fruit, Flower):
        def apple_benefits(self):
            print("I am child class : Apple Benefits")

    #Object creation
    apple_fruit = Apple()
    #Access the parent method
    apple_fruit.fruits_benefits()
    #Access the parent method
    apple_fruit.flower_benefits()
    #Access the child method
    apple_fruit.apple_benefits()

 Output

    I am parent class 1 : Fruits Benefits
    I am parent class 2 : Flower Benefits
    I am child class : Apple Benefits

## **Multilevel Inheritance**
In multilevel inheritance, grandchild class inherits from child class which inherits from parent class in python

    #Parent class
    class Fruit:
        def fruits_benefits(self):
            print("I am parent class : Fruits Benefits")
            
    #Child class    
    class Apple(Fruit):
        def apple_benefits(self):
            print("I am child class : Apple Benefits")
            
    #Grandchild class
    class Breakfast(Apple):
        def breakfast_benefits(self):
            print("I am grandchild class : Breakfast Benefits")

    #Object creation
    breakfast = Breakfast()
    #Access the parent method
    breakfast.fruits_benefits()
    #Access the child method
    breakfast.apple_benefits()
    #Access the grandchild method
    breakfast.breakfast_benefits()

 Output

    I am parent class : Fruits Benefits
    I am child class : Apple Benefits
    I am grandchild class : Breakfast Benefits

## **Hierarchical Inheritance**
In Hierarchical inheritance, a parent class have multiple child classes

    #Parent class
    class Fruit:
        def fruits_benefits(self):
            print("I am parent class : Fruits Benefits")
            
    #Child class 1    
    class Apple(Fruit):
        def apple_benefits(self):
            print("I am child class 1 : Apple Benefits")

    #Child class 2
    class Orange(Fruit):
        def orange_benefits(self):
            print("I am child class 2 : Orange Benefits")

    #Object creation 1
    apple = Apple()
    apple.fruits_benefits()
    apple.apple_benefits()

    #Object creation 2
    orange = Orange()
    orange.fruits_benefits()
    orange.orange_benefits()

 Output

    I am parent class : Fruits Benefits
    I am child class 1 : Apple Benefits
    I am parent class : Fruits Benefits
    I am child class 2 : Orange Benefits

## **Hybrid Inheritance**
Its a combination of two or more above mentioned types of inheritance

Multiple and multilevel inheritance combination is an example for hybrid inheritance

    #Parent class
    class Fruit:
        def fruits_benefits(self):
            print("I am parent class : Fruits Benefits")
            
    #Child class 1    
    class Apple(Fruit):
        def apple_benefits(self):
            print("I am child class 1 : Apple Benefits")
            
    #Grandchild class
    class Breakfast(Apple):
        def breakfast_benefits(self):
            print("I am grand child class 1 : Breakfast Benefits")

    #Child class 2
    class Orange(Fruit):
        def orange_benefits(self):
            print("I am child class 2 : Orange Benefits")
            
    #Grandchild class
    class Lunch(Orange):
        def lunch_benefits(self):
            print("I am grand child class 1: Lunch Benefits")


    #Object creation 1
    breakfast = Breakfast()
    breakfast.fruits_benefits()
    breakfast.apple_benefits()
    breakfast.breakfast_benefits()

    #Object creation 2
    lunch = Lunch()
    lunch.fruits_benefits()
    lunch.orange_benefits()
    lunch.lunch_benefits()

 Output

    I am parent class : Fruits Benefits
    I am child class 1 : Apple Benefits
    I am grand child class 1 : Breakfast Benefits
    I am parent class : Fruits Benefits
    I am child class 2 : Orange Benefits
    I am grand child class 1: Lunch Benefits