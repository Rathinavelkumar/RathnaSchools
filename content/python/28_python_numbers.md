As mentioned in Python Data types section, Python provides the support for integers, floating and complex numbers. In this section, Lets learn the Math function and type conversion methods

## **Round Function**
Round function used to round the float number to nearest whole number

    #Round Function

    #Nearest whole number is 5
    print( round(5.1) )

    #Nearest whole number is 6
    print( round(5.8) )

    #Nearest even number considers for 0.5 cases
    print( round(6.5) )
    print( round(7.5) )

    #Rounding with second argument
    print( round(21.7777777777, 3) )

 Output

    5
    6
    6
    8
    21.778

## **Power Function**
Power function is similar to ** operator which we have learned in arithmetic operator section

    #Power Function

    #Below power function similar to 2*2*2*2*2
    print( pow(2, 5) )

    #Below power function similar to (2*2*2*2*2)%3
    print( pow(2, 5, 3) )

 Output

    32
    2

## **Absolute Function**
Absolute function helps to convert negative number into positive number

    #Absolute Function

    #Convert negative number to positive number 
    print( abs(-100) )

 Output

    100

## **Type Conversion**
Types conversion helps to covert the value from one data type to another data type

Two types of Type conversion in python:

1. Implicit Type Conversion
2. Explicit Type Conversion

**Implicit Type Conversion**
Python automatically converts the value from one data type to another

    #Implicit Type Conversion
    num1 = 5
    num2 = 3.5

    result = num1 + num2
    print(type(result))
    print(result)

 Output

    <class 'float'>
    8.5

**Explicit Type Conversion**
In some cases, user requires to change the type of the data explicitly before operation

    #Explicit Type Conversion
    num1 = 50
    num2 = "50"

    result = num1 + num2
    print(result)

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


Explicit conversion helps to overcome the type error

    #Explicit Type Conversion
    num1 = 50
    num2 = int("50")

    result = num1 + num2
    print(result)

 Output

    100