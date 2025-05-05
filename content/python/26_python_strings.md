In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding.

## **String Creation**
Python provides multiple number of ways to create a string literal

    #String Creation

    #Enclosed with single quotes
    single_quoted_data = 'I am created with single quote'
    print(single_quoted_data)

    #Enclosed with double quotes
    double_quoted_data = "I am created with double quotes"
    print(double_quoted_data)

    #Enclosed with triple single quotes
    triple_single_quoted_data = '''I am created
    with
    triple single quotes'''
    print(triple_single_quoted_data)

    #Enclosed with triple double quotes
    triple_double_quoted_data = """I am created
    with
    triple double quotes"""
    print(triple_double_quoted_data)

 Output

    I am created with single quote
    I am created with double quotes
    I am created
    with
    triple single quotes
    I am created
    with
    triple double quotes

## **String Reading**
Read a character with the help of positive and negative index value

| P  | Y  | T  | H  | O  | N  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

Every character have one positive and negative index in the string like the above example

    #String Reading
    school_name = "RATHNASCHOOLS"

    #Reading the first character of the string
    print(school_name[0])
    print(school_name[-13])

    #Reading the second character of the string
    print(school_name[1])
    print(school_name[-12])

    #Reading the last character of the string
    print(school_name[12])
    print(school_name[-1])

 Output

    R
    R
    A
    A
    S
    S

## **String Update**
Strings are immutable, which means that cannot update once created

    #String Update
    school_name = "RATHNASCHOOLS"

    #Item assignment impossible for immutable objects
    school_name[1] = "E"

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    TypeError: 'str' object does not support item  assignment

Recreation of entire object is the only way for update the immutable objects in python

    #String Update
    school_name = "RATHNASCHOOLS"

    #Object Recreation
    school_name = "RETHNASCHOOLS"
    print(school_name)

 Output
    
    RETHNASCHOOLS

## **String Deletion**
Strings are immutable, which means that cannot delete once created

    #String Deletion
    school_name = "RATHNASCHOOLS"

    #Item deletion impossible for immutable objects
    del school_name[0]

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    TypeError: 'str' object doesn't support item deletion

Entire object can delete but not a substring in python

    #String Deletion
    school_name = "RATHNASCHOOLS"

    #Entire object deletion is possible
    del school_name
    print(school_name)

## **String Slicing**
String slice helps to return the required substring for the given string

   **string_name(start Index: stop Index: step Value(optional)]**

   * `start Index Not declare means, first value index consider by python`

   * `stop Index Not declare means, last value index consider by python`

| P  | Y  | T  | H  | O  | N  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

    #String Slicing
    school_name = "RATHNASCHOOLS"

    #Print the first three characters
    print(school_name[0:3])
    print(school_name[-13:3])
    print(school_name[:3])

    #Print the middle three characters
    print(school_name[6:9])
    print(school_name[-7:9])

    #Print the last two characters
    print(school_name[11:13])
    print(school_name[-2:13])
    print(school_name[11:])

 Output

    RAT
    RAT
    RAT
    SCH
    SCH
    LS
    LS
    LS
