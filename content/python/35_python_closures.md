Before knowing the decorator concepts, its good to know about python closures


## **Closure conditions**
To implement closures in python, below conditions should be matched 

1. It should have a nested Function
2. Nested function should have a argument which pass from an enclosing(outer) function
3. Nested function should be called inside outer function


## **Nested function**
Below is the best and simple example to understand the Nested Function and python closures. Nested function can access the enclosed function variable without global declaration

    #Nested Function
    def outer_function(name):
        def inner_function():
            print("The name is {}".format(name))
        inner_function()

    outer_function("Rathna Schools")

 Output

    The name is Rathna Schools

## **Closure creation**
Python closure stores the inner function state in a variable and call them whenever required like below

    #Python Closures
    def outer_function(name):
        def inner_function():
            print("The name is {}".format(name))
        return inner_function

    result = outer_function("Rathna Schools")
    #result variable behaves as independent inner function
    result()

    #Even though we deletes the outer function, closure variable survives in memory
    del outer_function
    result()


 Output

    The name is Rathna Schools
    The name is Rathna Schools

## **When to use**
Instead of using class for simple scenario, closure serves like better than class implementation like the below example

    #Python Closures
    def ten_multiples(input_num):
        def multiply():
            print(input_num*10)
        return multiply

    result1 = ten_multiples(2)
    result1()
    result2 = ten_multiples(5)
    result2()

 Output

    20
    50

As mentioned at beginning, decorators are extremely leveraging the benefits of closures. It is explained in next tutorial with simple examples