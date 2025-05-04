Various built-in functions are available in Python which helps to perform multiple operations on string. Below are the top must know string methods in python

## **Built-In Functions**

* `upper()` - converts the given string to uppercase

* `lower()` - converts the given string to lowercase

* `len()` - Returns the length of the given string

Below simple program shows the use case of all functions

    #String Functions
    school_name = "Rathna Schools"

    #Upper Method
    print(school_name.upper())

    #Lower Method
    print(school_name.lower())

    #Length Function
    print("Length of given string is : {}".format(len(school_name)))

 Output

    RATHNA SCHOOLS
    rathna schools
    Length of given string is : 14

## **Boolean Methods**

* `isupper()` - returns true if all the characters in given string are uppercase

* `islower()` - returns true if all the characters in given string are lowercase

* `isalpha()` - returns true if all the characters in given string are alphabets

* `isnumeric()` - returns true if all the characters in given string are number

* `isalnum()` - returns true if all the characters in given string are alphanumeric

Below simple program shows the use case of all boolean methods

    #Boolean Methods

    #Isupper method
    school_name = "RATHNA SCHOOLS"
    print(school_name.isupper())

    #Islower method
    school_name = "rathna schools"
    print(school_name.islower())

    #Isalpha method
    school_name = "RathnaSchools"
    print(school_name.isalpha())

    #Isnumeric method
    register_number = "12345"
    print(register_number.isnumeric())

    #Isalnum method
    user_name = "RathnaSchools12345"
    print(register_number.isalnum())

 Output

    True
    True
    True
    True
    True

## **Reusable Methods**

* `split()` - helps to split the given string with given character

* `join()` - helps to join the given character with existing each character of given string

* `replace()` - helps to replace the old characters of given string with new character

* `find()` - returns the first occurrence of the specified value, if not available -1 will returns


Below simple program shows the use case of all reusable methods

    #Reusable Methods

    #Split Method
    school_name = "RATHNA SCHOOLS"
    splitted_list = school_name.split()
    print(splitted_list)

    #Join Function
    joined_school_name = " ".join(splitted_list)
    print(joined_school_name)

    #Replace Method
    replaced_school_name = joined_school_name.replace(" ","|")
    print(replaced_school_name)

    #Find Method
    print(school_name.find("R"))
    #First instance considers incase of multiple occurrence
    print(school_name.find("S"))
    #Returns -1 when no occurrence found
    print(school_name.find("z"))

 Output

    ['RATHNA', 'SCHOOLS']
    RATHNA SCHOOLS
    RATHNA|SCHOOLS
    0
    7
    -1