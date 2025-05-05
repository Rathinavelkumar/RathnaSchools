Python is a multi-paradigm programming language which means, it supports to implement both object oriented programing and procedural programming in python 

## **What is OOPs**
OOPS is a very famous and popular programming paradigm. It deals with the concept of classes and object where classes are consider as blueprints, based on that object can be created as individual instances. In upcoming sections, we will see the below important OOP concepts with real time programming examples

* **`Class`** 
* **`Object`**
* **`Method`**
* **`Inheritance`**
* **`Encapsulation`**
* **`Polymorphism`**
* **`Data Abstraction`**

## **Class, Object and Method**
Object is a group of variables and methods where class is the blueprint of that object

REALTIME EXAMPLE:
Project Name : Fruits Database

    ############# Class Blueprint ###############
    class FruitsDatabase:
        #Class attributes
        database_type = "fruits"
        
        #Constructor
        def __init__(self, name):
            self.name = name
        
        #Method
        def list_the_usage(self, benefits):
            for each_benefit in benefits: print(each_benefit)

    ############# Object Creation - 1 ###############
    apple_fruit = FruitsDatabase("APPLE")
    apple_benefits = ["Healthy Immune system", "Diabetes-Friendly Fruit"]

    #Printing the required values
    print("####### APPLE DATA #######")
    print(apple_fruit.database_type)
    print(apple_fruit.name)
    apple_fruit.list_the_usage(apple_benefits)

    ############# Object Creation - 2 ###############
    orange_fruit = FruitsDatabase("ORANGE")
    orange_benefits = ["Protect your cell from damage", "Boosts your immune system"]

    #Printing the required values
    print("####### ORANGE DATA #######")
    print(orange_fruit.database_type)
    print(orange_fruit.name)
    orange_fruit.list_the_usage(orange_benefits)

    ############# Object Creation - 3 ###############
    mango_fruit = FruitsDatabase("MANGO")
    mango_benefits = ["Improve Digestive Health", "High in Antioxidants", "Improve hair and skin health"]

    #Printing the required values
    print("####### MANGO DATA #######")
    print(mango_fruit.database_type)
    print(mango_fruit.name)
    mango_fruit.list_the_usage(mango_benefits)

 Output

    ####### APPLE DATA #######
    fruits
    APPLE
    Healthy Immune system
    Diabetes-Friendly Fruit
    ####### ORANGE DATA #######
    fruits
    ORANGE
    Protect your cell from damage
    Boosts your immune system
    ####### MANGO DATA #######
    fruits
    MANGO
    Improve Digestive Health
    High in Antioxidants
    Improve hair and skin health