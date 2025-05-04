As mentioned in previous chapter, python should use the def keyword to create functions but anonymous function can be create using lambda keyword. It should have only one expression, but we can pass multiple arguments

## **Lambda vs Normal Functions**
Normal Function - To create multiple of ten for given number

    #Normal Function
    def calc(num):
        result = num * 10
        return result

    output = calc(5)
    print(output)

 Output

    50

Lambda function - To create multiple of ten for given number

    #Lambda Function
    calc = lambda x : x*10

    output = calc(5)
    print(output)

 Output

    50

## **Lambda with multiple argument**
We can pass multiple arguments to lambda functions

    #Lambda function with multiple arguments
    add = lambda x, y : x+y

    output = add(50, 100)
    print(output)

Output

    150

## **Lambda with map function**

    #Lambda function along with map
    data = [1, 2, 3, 4, 5]
    output = list(map(lambda x : x*10, data))
    print(output)

 Output

    [10, 20, 30, 40, 50]

## **Lambda with filter function**

    #Lambda function with filter
    data = [1, 2, 3, 4, 5]
    #Filter and return only even number in given list
    output = list(filter(lambda x : x%2==0, data))
    print(output)

 Output

    [2, 4]