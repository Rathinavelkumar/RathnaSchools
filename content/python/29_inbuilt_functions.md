The top must known inbuilt function in python are

## **Abs Function**
Abs function helps to return the absolute value of given number

    #Abs Function
    input_value = -50

    output_value = abs(input_value)
    print(output_value)

 Output

    50

## **All Function**
All function checks all the elements in the given iterable is true or not

    #All Function
    input_value = [10, 20, 30, 40]

    output_value = all(input_value)
    print(output_value)

 Output

    True

Zero or False value in the given input returns false

    #All Function
    input_value = [10, 20, 30, 0]

    output_value = all(input_value)
    print(output_value)

 Output

    False

## **Any Function**
Any function returns true if any one of the element is true in given iterable

    #Any Function
    input_value = [10, 20, 30, 0]

    output_value = any(input_value)
    print(output_value)

 Output

    True

## **ASCII(Ord) Function**
Ord function helps to return the ASCII (American Standard Code for Information value of given character Interchange)

    #Ord Function
    input_value = "R"

    output_value = ord(input_value)
    print(output_value)

 Output

    82

## **Bin Function**
Bin function helps to convert the decimal number to a binary string. Result have `ob` prefix which indicates the binary format

    #Bin Function
    input_value = 10

    output_value = bin(input_value)
    print(output_value)

 Output

    0b1010

## **Bool Function**
Bool functions returns the Boolean value (i.e.) either true or false

    #Bool Function
    input_value1 = 0
    input_value2 = 1

    output_value1 = bool(input_value1)
    print(output_value1)

    output_value2 = bool(input_value2)
    print(output_value2)

 Output

    False
    True

## **Breakpoint Function**
In python 3.7, breakpoint function has introduced which helps to invoke breakpoint without import of pdb module. Previously we can use the pdb module, in which pdb.set_trace() function act as a breakpoint

    #Breakpoint Function
    input_value1 = 0
    input_value2 = 1

    output_value1 = bool(input_value1)
    print(output_value1)


    output_value2 = bool(input_value2)
    print("Want to continue? Press c and Enter")
    breakpoint()
    print(output_value2)

 Output

    False
    Want to continue? Press c and Enter
    > <string>(12)<module>()
    (Pdb) c
    True

## **Bytearray Function**
As per python documentation, Bytearray function Return a new array of bytes. The bytearray type is a mutable sequence of integers in the range 0 < x < 256.

**source [optional]: byte array initializer**

**encoding [optional]: string encoding method**

**errors [optional]: steps to perform during failure of encoding**

    #ByteArray Function
    input_data = "RATHNA SCHOOLS"

    output1 = bytearray(input_data, "utf-8")
    print(output1)

    output2 = bytearray(input_data, "utf-16")
    print(output2)

 Output

    bytearray(b'RATHNA SCHOOLS')
    bytearray(b'\xff\xfeR\x00A\x00T\x00H\x00N\x00A\x00 \x00S\x00C\x00H\x00O\x00O\x00L\x00S\x00')

## **Bytes Function**
Byte function is similar to bytearray but they returns a immutable bytes object, so it cannot be changed once declared

    #Bytes Function
    input_data = "RATHNA SCHOOLS"

    output1 = bytes(input_data, "utf-8")
    print(output1)

    output2 = bytes(input_data, "utf-16")
    print(output2)

 Output

    b'RATHNA SCHOOLS'
    b'\xff\xfeR\x00A\x00T\x00H\x00N\x00A\x00 \x00S\x00C\x00H\x00O\x00O\x00L\x00S\x00'

## **Callable Function**
Callable function helps to check whether the given object argument is callable or not

    #Function1
    def add():
        return "add function"
        
    #Function2
    def sub():
        return "sub function"
        
    #Variable
    mul = "mul function"
        
    print(callable(add))
    print(callable(sub))
    #Its variable, not a callable function
    print(callable(mul))

 Output

    True
    True
    False

## **Chr Function**
Chr function helps to convert the ASCII value to its original character 

    #Chr Function
    input_data = "R"

    #convert to ASCII value
    output_value1 = ord(input_data)
    print(output_value1)

    #Convert back to original character
    output_value2 = chr(output_value1)
    print(output_value2)

 Output

    82
    R

## **Compile Function**
Compile method helps to convert the source code to an executable, so that it can execute whenever required

**syntax - compile(source, filename, mode)**

**source - source code (it can single line or complete block**

**filename - source code reading filename, if not we can pass random name**

**mode - eval mode in case of single line, exec can use for multi line source code**

    #Compile Function
    source_code = "print('RATHNA SCHOOLS')"

    compile_code = compile(source_code, "Test", "eval")

    eval(compile_code)

 Output

    RATHNA SCHOOLS

## **Complex Function**
Complex function used to covert the string or number into a complex number 

    #Complex Function
    input_data1 = complex(5,10)
    print(input_data1)

    input_data2 = complex(5)
    print(input_data2)

 Output

    (5+10j)
    (5+0j)

## **Deltattr Function**
Deltattr function helps to delete the named attribute from the given object which should be allows it

    #Delattr Function
    class Score:
        python = 100
        js = 90
        java = 80
        
    #Object Creation
    score_object = Score()

    #Before Deletion
    print(score_object.python)
    print(score_object.js)
    print(score_object.java)

    #After Deletion
    delattr(Score, 'java')
    print(score_object.python)
    print(score_object.js)
    print(score_object.java)

 Output

    100
    90
    80
    100
    90
    Traceback (most recent call last):
    File "<string>", line 19, in <module>
    AttributeError: 'Score' object has no attribute 'java'

## **Dict Function**
Dict Function helps to create a new dictionary

    #Dict Function
    input_dict = dict(
        Name = "Rathna Schools",
        Language = "Python"
        )

    print(input_dict)

 Output

    {'Name': 'Rathna Schools', 'Language': 'Python'}

## **Dir Function**
Dir function is one of the most important built-in function in python.

without parameter -  It helps to return the list of name in current local scope

with parameter - it helps to list the valid methods of given object in current local scope 

    #Dir Function
    print("Without parameter")
    print(dir())

    print("With Parameter")
    input_data = list()
    print(dir(input_data))

 Output

    Without parameter
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
    With Parameter
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

## **Divmod Function**
Divmod function takes two arguments and return its quotient and remainder

    #Divmod Function
    input_value = 19
    target_value = 3

    result = divmod(input_value, target_value)
    print(result)

 Output

    (6, 1)

## **Enumerate Function**
Enumerate function helps to create enumerate object by adding counter to iterable from 0 index

    #Enumerate Function
    month_list = ["Jan", "Feb", "Mar"]

    result = list(enumerate(month_list))
    print(result)
 
 Output

    [(0, 'Jan'), (1, 'Feb'), (2, 'Mar')]

## **Eval Function**
Eval function helps to evaluates the single expression and return the calculated result of that corresponding expression

    #Eval Function
    statement = "print('Rathna Schools')"
    eval(statement)

 Output

    Rathna Schools

## **Exec Function**
Exec function helps to evaluates the one or more expression and return the calculated result of that corresponding expression or statement

    #Exec Function
    statement = "for _ in range(0,3):\n\tprint('Rathna Schools')"
    exec(statement)

 Output

    Rathna Schools
    Rathna Schools
    Rathna Schools

## **Filter Function**
Filter function usually accepts two parameter, a function which should check each elements and the sequence which is needs to gets filtered 

    #Filter Function
    def find_even(num):
        if num%2==0: return True

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(find_even, input_list))
    print(result)

 Output

    [2, 4, 6, 8, 10]

## **Format Function**
Format function helps to handle the complex string formatting representation easily in python

    input_name = "Rathna Schools"

    #Format Function Different Use Cases
    print("Learn Python - {0}".format(input_name))
    print("Learn Python - {}".format(input_name))
    print("The sum of {0} + {1} is {2}".format(50, 100, 50+100))
    print("The sum of {} + {} is {}".format(50, 100, 50+100))
    print("The sum of {num1} + {num2} is {result}".format(num1=50, num2=100, result=50+100))
    print("The sum of {num1} + {num2} is {result}".format(num2=100, result=50+100, num1=50))

 Output

    Learn Python - Rathna Schools
    Learn Python - Rathna Schools
    The sum of 50 + 100 is 150
    The sum of 50 + 100 is 150
    The sum of 50 + 100 is 150
    The sum of 50 + 100 is 150

## **Hash Function**
Hash function helps to convert the given immutable data into hashable value

    #Hash Function
    input_name = "Rathna Schools"
    encoded_result = hash(input_name)
    #Every time generate new value
    print(encoded_result)

    #Immutable data raises exception
    input_list = [1, 2, 3, 4, 5]
    encoded_list = hash(input_list)
    print(encoded_list)

 Output

    6055507806959227419
    Traceback (most recent call last):
    File "<string>", line 9, in <module>
    TypeError: unhashable type: 'list'

## **Hex Function**
Hex function helps to covert the given integer number to hexa decimal value

    #Hex Function
    input_num = 100
    result = hex(input_num)
    print(result)

 Output

    0x64

## **Id Function**
Id function helps to return the address of the given object in memory. As per python documentation, two objects with non-overlapping lifetimes may have the same id value.

    #Id Function
    input_num1 = 100
    result1 = id(input_num1)
    print(result1)

    #Immutable data types with same value, have same memory location
    input_num2 = 100
    result2 = id(input_num2)
    print(result2)

    #If we change the value, then memory location changes
    input_num2 = 50
    result2 = id(input_num2)
    print(result2)

 Output

    9792160
    9792160
    9790560

## **Input Function**
input() helps to interact with user and get the user's input in string format

    #Input Function
    input_name = input("Please enter the name : ")
    print(input_name)

 Output

    Please enter the name : Rathna Schools
    Rathna Schools

## **Iter Function**
Iter function helps to convert the given sequence to iterator object. To access the elements in iterator we can use the next() function

    #Iter Function
    months = ["Jan" , "Feb", "Mar", "Apr"]
    iter_months = iter(months)
    try:
        while iter_months:
            print(next(iter_months))
    except StopIteration:
        print("completed")

 Output

    Jan
    Feb
    Mar
    Apr
    completed

## **Locals Function**
Locals function helps to return a dict value of current local symbol table

    #Locals Function
    def func_without_local():
        print(locals())

    def func_with_local():
        name = "Rathna Schools"
        print(locals())

    #Return empty dict
    func_without_local()

    #Return local variable dict
    func_with_local()

 Output

    {}
    {'name': 'Rathna Schools'}

## **Map Function**
Map function helps to apply the function and yield the results of each item in given sequence

    #Map Function
    def two_multiple(num):
        return num*2

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(two_multiple, input_list))
    print(result)

 Output

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

## **Object Function**
Object function helps to return a new feature less object which can be a base of all classes

    #Object Function
    obj_example =  object()
    print(type(obj_example))
    print(id(obj_example))

 Output

    <class 'object'>
    140529277524880

## **Repr Function**
Repr functions are similar to str() function but it return the printable string representation of the given object

    #Repr Function
    input_name = "Rathna's Schools"
    print(str(input_name))
    print(repr(input_name))

 Output

    Rathna's Schools
    "Rathna's Schools"

## **Reversed Function**
Reversed function helps to reverse the given iterable and returns the reversed iterator

    #Reversed Function
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(reversed(input_list)))

 Output

    [9, 8, 7, 6, 5, 4, 3, 2, 1]

## **Slice Function**
Slice function helps to return slice object from any sequence object like string, list, tuple etc..

**Syntax**

**slice(start, stop, step)**

    #Slice Function
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #Different Use Cases
    print(input_list[0:5])
    print(input_list[3:8])
    print(input_list[0:10:2])

 Output

    [1, 2, 3, 4, 5]
    [4, 5, 6, 7, 8]
    [1, 3, 5, 7, 9]

## **Zip Function**
zip(*iterable) function helps to return a ZIP object. we can pass multiple iterables as parameter to ZIP function in order to create a single zip object

    #Zip Function
    index_list = [1, 2, 3, 4, 5]
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index, month in zip(index_list, month_list):
        print(index, month)

 Output

    1 Jan
    2 Feb
    3 Mar
    4 Apr
    5 May