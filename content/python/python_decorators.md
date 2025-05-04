Decorators are used to modify the existing functionality without changing the existing code of that function. A function is modify with another function  at compile time is also called as meta programming

## **Simple Decorators**
Like the below example, we can implement the decorators for the normal function to implement more functionality

    #Normal Function without decorators
    def school_name(name):
        print("The school name is {}".format(name))
        
    school_name("Rathna Schools")

 Output

    The school name is Rathna Schools

Incase, business request to implement pretty text for the existing function means, we can develop decorator like below to extend its functionality without modification in it

    #Decorator Implementation
    def simple_decorator(func):
        def make_pretty(input_data):
            print("Make Pretty - Implementation")
            func(input_data)
        return make_pretty
        
    @simple_decorator
    def school_name(name):
        print("The school name is {}".format(name))
        
    school_name("Rathna Schools")

 Output

    Make Pretty - Implementation
    The school name is Rathna Schools

## **Realtime Example 1**
Implementation of exception handling decorators like the below example to handle exception

    #Normal function without any exception
    def divide(dividend, divisor):
        print("The quotient is {}".format(str(dividend//divisor)))
        print("The remainder is {}".format(str(dividend%divisor)))

    #This work without any exception
    divide(100,3)

    #This raise zero division exception
    divide(75, 0)

 Output

    The quotient is 33
    The remainder is 1
    Traceback (most recent call last):
    File "<string>", line 7, in <module>
    File "<string>", line 3, in divide
    ZeroDivisionError: integer division or modulo by zero

Handle above exception with decorators without any modification in existing function

    #Exception handling decorators
    def exception_handler(func):
        def inner_func(num1, num2):
            try:
                func(num1, num2)
            except ZeroDivisionError:
                print("Divisor should not be Zero")
        return inner_func

    @exception_handler
    def divide(dividend, divisor):
        print("The quotient is {}".format(str(dividend//divisor)))
        print("The remainder is {}".format(str(dividend%divisor)))

    #This work without any exception
    divide(100,3)

    #Now this handles by exception handler decorator
    divide(75, 0)

 Output

    The quotient is 33
    The remainder is 1
    Divisor should not be Zero

## **Realtime Example 2**
Database connection decorator implementation for the required function to perform the database operation like the below example

    #DB connector decorator
    def make_connection(func):
        def inner_func(*args, **kwargs):
            print("DB connection - Successful")
            func(*args, **kwargs)
        return inner_func

    @make_connection
    def read_user(*args, **kwargs):
        query = "select * from {} where id={}".format(args[0], kwargs['user_id'])
        print(query)
        
    read_user("users", user_id="1234")

 Output

    DB connection - Successful
    select * from users where id=1234