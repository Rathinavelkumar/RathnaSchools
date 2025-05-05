Lists are used to store multiple items in a single variable. They are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in Python

## **List Creation**
List created by declare all the items inside the square brackets []

    #List Creation
    languages = ["Python", "Java", "Javascript"]
    print(type(languages))

    #Multiple data types can store in list
    user_details = [1, "PYTHON", "99.0", ["Jan", "Feb"]]
    print(user_details)

 Output

    <class 'list'>
    [1, 'PYTHON', '99.0', ['Jan', 'Feb']]

## **List Reading**
List items can be read with the help of positive or negative index of that corresponding position

| "Jan"  | "Feb"  | "Mar"  | "Apr"  | "May"  | "Jun"  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

Every item in the list have both positive and negative index like the above table

    #List Reading
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    #Reading the first item of the list
    print(month_list[0])
    print(month_list[-6])

    #Reading the second item of the list
    print(month_list[1])
    print(month_list[-5])

    #Reading the last item of the list
    print(month_list[5])
    print(month_list[-1])

 Output

    Jan
    Jan
    Feb
    Feb
    Jun
    Jun

## **List Update**
List are mutable data types in python, so we can perform the update operation. No need to create new object for modification

    #List Update
    month_list = ["Jan", "Dec", "Mar", "Apr", "May", "Jun"]
    print(id(month_list))

    #Update using index of the item
    month_list[1] = "Feb"
    print(month_list)
    print(id(month_list))

 Output

    140324018130432
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    140324018130432

## **List Deletion**
Since list are mutable data types in python, we can perform the delete operation without delete the entire object and recreate for the few deletion

    #List Deletion
    month_list = ["Jan", "Dec", "Feb", "Mar", "Apr", "May", "Jun"]
    print(id(month_list))

    #Deletion using index of the item
    month_list.remove("Dec")
    print(month_list)
    print(id(month_list))

 Output

    139779868761664
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    139779868761664

Since list is immutable data type, id of the list object not changed even after deletion

## **List Slicing**
List slicing helps to return the required objects from the given list

**ListName(start Index: stop Index: step Value (optional)]**

* `start Index Not declare means, first value index consider by python`

* `stop Index Not declare means, last value index consider by python`

Read a object with the help of positive and negative index value

| "Jan"  | "Feb"  | "Mar"  | "Apr"  | "May"  | "Jun"  |
| :--|:--:| --:| --:| --:| --:|
| 0  | 1  | 2  | 3  | 4  | 5  |
| -6 | -5 | -4 | -3 | -2 | -1 |

    #List Slicing
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

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

    ['Jan', 'Feb']
    ['Jan', 'Feb']
    ['Jan', 'Feb']
    ['Mar', 'Apr']
    ['Mar', 'Apr']
    ['May', 'Jun']
    ['May', 'Jun']
    ['May', 'Jun']
