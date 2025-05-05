In this part, we are going to deep dive about different types of arguments in functions

Below are the types of arguments

* **`Default Arguments`**
* **`positional Arguments`** 
* **`Keyword Arguments`** 
* **`Arbitrary Positional Arguments`** 
* **`Arbitrary keyword arguments`** 

## **Default Arguments**
Function Definition with default value for num2 and non-default value for num1

Default argument should be declare after the Non-default arguments

    #Default Arguments
    #num2 is default argument here
    def add(num1, num2=100):
        value1 = num1
        value2 = num2
        sum = value1 + value2
        return sum

    #Function Calling 
    result = add(10, 20)
    print(result)

    #Default argument is optional
    result = add(50)
    print(result)

 Output

    30
    150

## **Positional Arguments**
When we are calling the function, the order of passing arguments should be matched with the order of parameters in function definition

    #positional Arguments
    def add(num1, num2:
        value1 = num1
        value2 = num2
        sum = value1 + value2
        return sum

    #Function Calling 
    #Automatically 10 is assigns with num1 and 20 is assigns with num2
    result = add(10, 20)
    print(result)

 Output

    30
    150

## **Keyword Arguments**
In keyword arguments, we can change the order of the arguments by explicitly mentioned the function parameter name

    #Keyword Arguments
    def add(num1, num2):
        value1 = num1
        value2 = num2
        print("The value of num1 is : {}".format(num1))
        print("The value of num2 is : {}".format(num2))
        sum = value1 + value2
        return sum

    #Function Calling with keyword arguments
    result = add(num2=10, num1=20)
    print(result)

 Output

    The value of num1 is : 20
    The value of num2 is : 10
    30

## **Arbitrary Positional Arguments**
When we are unsure on the number of parameters should be declare during function definition, asterisk (*) can place to get the dynamic positional arguments

    #Arbitrary Positional Arguments
    def add(*args):
        sum=0
        for each in args:
            sum = sum + each
        return sum

    #Function Calling with Arbitrary Positional Arguments
    result = add(10, 20, 30)
    print(result)

 Output

    60

## **Arbitrary Keyword Arguments**
Double asterisk (**) can place to get the dynamic keyword arguments 

    #Arbitrary Keyword Arguments
    def add(**args):
        sum=0
        for key, value in args.items():
            print(key, value)
            sum = sum + value
        return sum

    #Function Calling with Arbitrary Keyword Arguments
    result = add(num1=10, num2=20, num3=30)
    print(result)

 Output

    num1 10
    num2 20
    num3 30
    60