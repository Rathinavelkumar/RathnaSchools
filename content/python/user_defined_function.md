Functions are organized reusable code block, which can be called whenever we required in our program. It helps to chunk our large program into smaller code blocks and provides greater re-usability

## **User defined function**
These functions creates by user for perform customized task.
Below are the major types of ways, we can create a user defined functions in python

## **Function Creation without Arguments**
def keyword helps to create functions in python

    #Function definition
    def add():
        value1 = 10
        value2 = 30
        sum = value1 + value2
        print(sum)

    #Function Calling 
    add()

    #Function can call how many times we required
    add()

 Output

    40
    40

## **Function Creation with Arguments**
Arguments helps to pass the values to the functions dynamically

    #Function definition
    def add(num1, num2):
        value1 = num1
        value2 = num2
        sum = value1 + value2
        print(sum)

    #Function Calling 
    add(10, 20)

    #Function calling with different parameter values
    add(50, 100)

 Output

    30
    150

## **Function Creation with return values**
Return keywords helps to return the required value from a function 

    #Function definition
    def add(num1, num2):
        value1 = num1
        value2 = num2
        sum = value1 + value2
        return sum

    #Function Calling 
    result = add(10, 20)
    print(result)

    #Function calling with different parameter values
    result = add(50, 100)
    print(result)

 Output

    30
    150