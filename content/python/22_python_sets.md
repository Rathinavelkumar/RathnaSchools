Sets are used to store multiple items in single variable as similar to list. But, Sets are unordered and not indexed and also has no duplicate elements.

## **Set Creation**
Set created by declare all the items inside the curly brackets {}

    #Set Creation
    languages = {"Python", "Java", "Javascript"}
    print(type(languages))

    #Unordered and Non duplicated
    languages = {"Python", "Java", "Javascript", "Java"}
    print(languages)

 Output

    <class 'set'>
    {'Javascript', 'Python', 'Java'}

It can store any immutable (int, float, string etc..) data. It cannot store any mutable (like list) data which raises exception

    #Set Creation

    #Mutable data type(like list) addition raises exception
    user_details = {1, "PYTHON", "99.0", ["Jan", "Feb"]}
    print(user_details)

 Output

    Traceback (most recent call last):
    File "<string>", line 4, in <module>
    TypeError: unhashable type: 'list'

## **Set Reading**
Since sets are unordered and unindexed, we cannot read the element using index which raises exception

    #Set Reading
    languages = {"Python", "Java", "Javascript"}
    print(languages[0])

 Output

    Traceback (most recent call last):
    File "<string>", line 3, in <module>
    TypeError: 'set' object is not subscriptable

We need to loop each and every element and access the set objects

    #Set Reading
    languages = {"Python", "Java", "Javascript"}

    #Looping each element and print the same
    for each in languages: print(each)

 Output

    Python
    Javascript
    Java

## **Set Update**
In sets, we cannot update the specific element, but we can append items from another set since they are mutable in nature

    #Set Update
    languages = {"Python", "Java", "Javascript"}
    languages[4] = "C++"

 Output

    Traceback (most recent call last):
    File "<string>", line 3, in <module>
    TypeError: 'set' object does not support item assignment

But, We can add the new set to the existing set since they are mutable in nature

    #Set Update
    languages = {"Python", "Java", "Javascript"}

    #Adding new set to existing set
    languages_new = {"C++", "R"}
    languages.update(languages_new)
    print(languages)

 Output

    {'C++', 'Java', 'Python', 'Javascript', 'R'}

## **Set Deletion**
In sets, we can perform the specific deletion as like in list using either remove or discard function

    #Set Deletion
    languages = {"Python", "Java", "Javascript"}

    #Remove Function
    languages.remove("Java")
    print(languages)

 Output

    {'Python', 'Javascript'}


Remove function - throws error if the element not available in the given set

    #Set Deletion
    languages = {"Python", "Java", "Javascript"}

    #Remove method raises exception for missing key
    languages.remove("C++")

 Output

    Traceback (most recent call last):
    File "<string>", line 5, in <module>
    KeyError: 'C++'


Discard function - won't throws the error if the set is not available in given set

    #Set Deletion
    languages = {"Python", "Java", "Javascript"}

    #Discard method won't raises exception for missing key
    languages.discard("C++")
    print(languages)

 Output

    {'Java', 'Javascript', 'Python'}

## **Set Slicing**
Since sets are unordered and unindexed, we cannot slice the set element using index

    #Set slicing
    languages = {"Python", "Java", "Javascript"}
    print(languages[:2])

 Output

    Traceback (most recent call last):
    File "<string>", line 3, in <module>
    TypeError: 'set' object is not subscriptable

We need to loop each and every element and access the set objects

    #Set slicing
    languages = {"Python", "Java", "Javascript"}

    #Looping each and print the element
    for each in languages: print(each)

 Output

    Java
    Python
    Javascript