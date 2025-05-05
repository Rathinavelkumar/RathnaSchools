Data types specify the different sizes and values that can be stored in the variable. Each and everything is an object in Python programming language, so below data-types are classes and the variables are instance of that classes.

## **Built-In Data Types**

    Numeric Types           # int, float and complex
    Text Type               # str
    Sequence Types          # list, tuple, range
    Mapping Type            # dict
    Set Types               # set, frozenset
    Boolean Type            # bool
    Binary Types            # bytes, bytesarray, memoryview

** `Note` - you can use any online python interpreter to run and test the below python programs

## **Numeric Data Types**
There are three distinct numeric types: integers, floating point numbers, and complex numbers. They are defined as int, float and complex classes in Python.

    #Numeric data types
    num1 = 5
    print(type(num1))

    num2 = 5.0
    print(type(num2))
    
    num3 = 5+2j
    print(type(num3))

 Output

    <class 'int'>
    <class 'float'>
    <class 'complex'>


## **Text Data Type**
Textual data in Python is handled with str objects, or strings. 

    #String data type
    name = "RATHNA SCHOOLS"
    print(type(name))

    #String literals are written in a variety of ways
    data = 'allows embedded "double" quotes'
    print(data)

    data = "allows embedded 'single' quotes"
    print(data)
    
 Output

    <class 'str'>
    allows embedded "double" quotes
    allows embedded 'single' quotes


## **Sequence Data Types**
There are three basic sequence types: lists, tuples, and range objects

    #List data type
    #Mutable (values can be change after declaration)
    list_data = [1, 5.0, "RATHNA SCHOOLS"]
    print(type(list_data))

    #Tuple data type
    #Immutable (values cannot be change after declaration)
    tuple_data = (1, 5.0, "RATHNA SCHOOLS")
    print(type(tuple_data))

    #Range data type
    range_data = range(1, 10)
    print(type(range_data))
    
 Output

    <class 'list'>
    <class 'tuple'>
    <class 'range'>


## **Mapping Data Type**
Dictionary is an unordered collection of key-value pairs. Dictionaries can be created by placing a comma-separated list of key: value pairs within braces

    #Dict data type
    dict_data = {"ID":12345, "Name": "RATHNA SCHOOLS"}
    print(type(dict_data))
    print(dict_data["ID"])
    print(dict_data["Name"])    

 Output

    <class 'dict'>
    12345
    RATHNA SCHOOLS

## **Set Data Types**
A set is an unordered collection of items. Major use case with set are membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference

    #Set data types
    set_data = {1, 2.0, "Rathna Schools"}
    print(set_data)
    #Elements can add after declaration
    set_data.add("5")
    print(set_data)

    #Frozen set
    Months = ["Jan", "Feb", "Mar"]
    frozen_set_data = frozenset(Months)
    print(frozen_set_data)
    #Elements cannot add after declaration
    frozen_set_data.add("5")
    print(frozen_set_data)

 Output

    {'Rathna Schools', 1, 2.0}
    {'Rathna Schools', 1, 2.0, '5'}
    frozenset({'Mar', 'Jan', 'Feb'})
    Traceback (most recent call last):
    File "<string>", line 13, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'


## **Boolean Data Type**
Boolean data type can be used to test the truth value. It always return either True or False as output which can be used in conditional and looping statements 

    #Bool data types
    bool_data = True
    print(type(bool_data))
    print(bool_data)

 Output

    <class 'bool'>
    True

## **Binary Data Types**
Bytes and Bytearray are used for manipulating binary data. The memoryview uses the buffer protocol to access the memory of other binary objects without needing to make a copy

    #Binary data types

    #Byte
    byte_data = b'RATHNA SCHOOLS'
    print(type(byte_data))
    print(byte_data)

    #Byte Array
    byte_array_data = bytearray(byte_data)
    print(type(byte_array_data))
    print(byte_array_data)

    #Memoryview
    memoryview_data = memoryview(byte_data)
    print(type(memoryview_data))
    print(memoryview_data)

 Output
 
    <class 'bytes'>
    b'RATHNA SCHOOLS'
    <class 'bytearray'>
    bytearray(b'RATHNA SCHOOLS')
    <class 'memoryview'>
    <memory at 0x7f814b6b9280>