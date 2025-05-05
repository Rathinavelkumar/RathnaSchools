Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

## **Dictionary Creation**
Dictionary can create using curly brackets with keys(should have only immutable data type-string, tuple, int) and values(accept all data types) 

    #Dictionary Creation
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript"
    }

    print("Dictionary Creation : ")
    print(language_dict)

 Output

    Dictionary Creation : 
    {1: 'Python', 2: 'Java', 3: 'JavaScript'}

Key should be unique - duplicate key creation replace the existing Value

    #Dictionary Creation
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        1 : "C++"
    }

    print("Duplicate keys overrides: ")
    print(language_dict)

 Output

    Duplicate keys overrides: 
    {1: 'C++', 2: 'Java', 3: 'JavaScript'}

## **Dictionary Access**
To access dictionary - we can use the key and value function or iterating each items in the given dictionary

    #Dictionary Access
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
    }

    print("Access using key : ")
    print(language_dict[1])

    print("Iteration - To access all value")
    for key, value in language_dict.items():
        print(key, value)

 Output

    Access using key : 
    Python
    Iteration - To access all value
    1 Python
    2 Java
    3 JavaScript

## **Dictionary update**
Dictionary can be update using the update function

    #Dictionary Update
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
    }

    print("Update using key : ")
    language_dict[1] = "C++"
    print(language_dict)

    print("Update using update method")
    language_dict.update({1 : "Python"})
    print(language_dict)

 Output

    Update using key : 
    {1: 'C++', 2: 'Java', 3: 'JavaScript'}
    Update using update method
    {1: 'Python', 2: 'Java', 3: 'JavaScript'}

## **Dictionary update**
Since dictionary is mutable, we can perform the specific deletion operation

    #Dictionary Update
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("Delete using key : ")
    language_dict.pop(4)
    print(language_dict)

    print("Delete using 'del' keyword")
    del language_dict[3]
    print(language_dict)

 Output

    Delete using key : 
    {1: 'Python', 2: 'Java', 3: 'JavaScript'}
    Delete using 'del' keyword
    {1: 'Python', 2: 'Java'}

## **Dictionary Slicing**
Since dictionary are unordered collection, we cannot perform the slicing operation in dictionary data

    #Dictionary Slicing
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("Dictionary slicing raises exception : ")
    print(language_dict[1:4])

 Output

    Dictionary slicing raises exception : 
    Traceback (most recent call last):
    File "<string>", line 10, in <module>
    TypeError: unhashable type: 'slice'