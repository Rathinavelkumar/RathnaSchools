Similar to lists, tuples are also used to store multiple object in a variable. But the tuples are fixed which cannot change once its created - IMMUTABLE data type.
It can store any type (int, float, string etc..) of data and they can be accessed using both positive and negative indexes as similar to list data

## **Tuple Creation**
Tuple created by declare all the items inside the round brackets ()

    #Tuple Creation
    languages = ("Python", "Java", "Javascript")
    print(type(languages))

    #Multiple data types can store in list
    user_details = (1, "PYTHON", "99.0", ["Jan", "Feb"])
    print(user_details)

    #In case of single item, comma is mandatory
    without_comma_item = ("Jan")
    with_comma_item = ("Jan",)
    print(type(without_comma_item), type(with_comma_item))

 Output

    <class 'tuple'>
    (1, 'PYTHON', '99.0', ['Jan', 'Feb'])
    <class 'str'> <class 'tuple'>

## **Tuple Reading**
As similar to list, tuple data items can be read with both positive ann negative index

| "Jan"  | "Feb"  | "Mar"  | "Apr"  | "May"  | "Jun"  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

Every item in the list have both positive and negative index like the above table

    #Tuple Reading
    month_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")

    #Reading the first item of the tuple
    print(month_list[0])
    print(month_list[-6])

    #Reading the second item of the tuple
    print(month_list[1])
    print(month_list[-5])

    #Reading the last item of the tuple
    print(month_list[5])
    print(month_list[-1])

 Output

    Jan
    Jan
    Feb
    Feb
    Jun
    Jun

## **Tuple Update**
Tuple are immutable data types in python, so we cannot perform the update operation

    #Tuple Update
    month_list = ("Jan", "Dec", "Mar", "Apr", "May", "Jun")

    #Update using index of the item raise exception
    month_list[1] = "Feb"

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    TypeError: 'tuple' object does not support item assignment

Needs to recreate the entire object due to its immutability

    #Tuple Update
    month_list = ("Jan", "Dec", "Mar", "Apr", "May", "Jun")
    print(id(month_list))

    #Recreating the entire object
    month_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")
    print(id(month_list))
    print(month_list)

 Output

    140186154916736
    140186155260128
    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')

## **Tuple Deletion**
Tuple are immutable data types in python, so we cannot perform the specific deletion which we can do in a list

    #Tuple Deletion
    month_list = ("Jan", "Dec", "Feb", "Mar", "Apr", "May", "Jun")

    #Specific element deletion raises exception
    month_list.remove("Dec")

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    AttributeError: 'tuple' object has no attribute 'remove'

Entire object requires to delete in Tuple in case of new modification

    #Tuple Deletion
    month_list = ("Jan", "Dec", "Feb", "Mar", "Apr", "May", "Jun")

    #Deletion the entire item
    del month_list
    print(month_list)

 Output

    Traceback (most recent call last):
    File "<string>", line 6, in <module>
    NameError: name 'month_list' is not defined

## **Tuple Slicing**
Tuple slicing helps to return the required objects from the given tuple

**TupleName(start Index: stop Index: step Value (optional)]**

* `start Index Not declare means, first value index consider by python`

* `stop Index Not declare means, last value index consider by python`

Read a object with the help of positive and negative index value

| "Jan"  | "Feb"  | "Mar"  | "Apr"  | "May"  | "Jun"  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

    #Tuple Slicing
    month_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")

    #Print the first two items
    print(month_list[0:2])
    print(month_list[-6:2])
    print(month_list[:2])

    #Print the middle two items
    print(month_list[2:4])
    print(month_list[-4:4])

    #Print the last two items
    print(month_list[4:6])
    print(month_list[-2:6])
    print(month_list[4:])

 Output

    ('Jan', 'Feb')
    ('Jan', 'Feb')
    ('Jan', 'Feb')
    ('Mar', 'Apr')
    ('Mar', 'Apr')
    ('May', 'Jun')
    ('May', 'Jun')
    ('May', 'Jun')