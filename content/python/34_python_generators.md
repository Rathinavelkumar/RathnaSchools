Generators helps to simplify the iterator concepts in python. The implementation of **iter** and **next** method is not required to build the traversal object in generator. With the help of **yield** keyword instead of **return** keyword. we can build iterable objects

## **Generators**
The same ten multiples concepts can be implement in generators with few lines of code like the below example.

    #Python Generators
    def TenMultipler(multiple, max_limit):
        start = multiple * 10
        for num in range(start, max_limit+1, start):
            yield num

    for each in TenMultipler(2, 100):
        print(each)

 Output

    20
    40
    60
    80
    100

## **Generator Expression**
Generator Expressions are awesome feature like list comprehension, we can build generator for the entire list without user-defined function. The generator expressions are more memory efficient since it will generate item only when requested but list comprehension generates the entire items during conversion itself

    input_list = [1, 2, 3, 4, 5]

    #Generator Expression
    result = ( each*10 for each in input_list )
    print("Output result from generator expression: ")
    #Generator item needs to generate one by one
    for each in result: print(each)

    #list comprehension
    result = [ each*10 for each in input_list ]
    print("Output result from list comprehension: ")
    #No need to generate one by one like generator expression
    print(result)

 output

    Output result from generator expression: 
    10
    20
    30
    40
    50
    Output result from list comprehension: 
    [10, 20, 30, 40, 50]