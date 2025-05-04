Various built-in functions are available in Python which helps to perform multiple operations on dictionary. Below are the top must know dict methods in python

## **Length Function**
This function helps to return the length of the given dictionary data items

    #Length Function
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("The length of the given dict datasets is : ")
    print(len(language_dict))

 Output

    The length of the given dict datasets is : 
    4

## **Clear Method**
Clear method helps to remove all the elements in given dict data items and make it as empty dict

    #Clear Method
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("The clear method removes all data...")
    language_dict.clear()
    print(language_dict)

 Output

    The clear method removes all data...
    {}

## **Get Method**
Get method helps to get the value for that specified key from given dict data items

    #Get Method
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("The get method retrieves the key's value...")
    print(language_dict.get(3))

 Output

    The get method retrieves the key's value...
    JavaScript

## **PopItem Method**
Popitem method helps to remove the last key value pair from dict by default

    #PopItem Method
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print("The popitem method removes the last item from dict...")
    language_dict.popitem()
    print(language_dict)

 Output

    The popitem method removes the last item from dict...
    {1: 'Python', 2: 'Java', 3: 'JavaScript'}

## **Copy Method**
Copy method helps to copy the given dict to another variable

    #Copy Method
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript",
        4 : "C++"
    }

    print(id(language_dict))
    print("Making a copy of dict data in different memory location")
    language_dict_copy = language_dict.copy()
    print(language_dict_copy)
    print(id(language_dict_copy))

 Output

    140312120052864
    Making a copy of dict data in different memory location
    {1: 'Python', 2: 'Java', 3: 'JavaScript', 4: 'C++'}
    140312120052928

## **Fromkeys Method**
Fromkey function helps to create dictionary from the given keys list and value

    #Fromkey Method
    language_keys = {1, 2, 3, 4}
    language_values = "Python"

    print("Creation of a dict using the fromkey method")
    language_dict = dict.fromkeys(language_keys, language_values)
    print(language_dict)

 Output

    Creation of a dict using the fromkey method
    {1: 'Python', 2: 'Python', 3: 'Python', 4: 'Python'}

## **SetDefault Method**
setDefault helps to return the given key's value as default. if the key is not available none will returns

    #SetDefault Method
    language_dict = {
        1 : "Python",
        2 : "Java",
        3 : "JavaScript"
    }

    #SetDefault returns the value of the corresponding key
    result=language_dict.setdefault(3)
    print(result)

    #None will return if the key is not available
    result=language_dict.setdefault(5)
    print(result) 

    #Create new pair, if we pass value also as a parameter
    result=language_dict.setdefault(4,"C++")
    print(language_dict)
    print(result)

 Output:

    JavaScript
    None
    {1: 'Python', 2: 'Java', 3: 'JavaScript', 5: None, 4: 'C++'}
    C++
