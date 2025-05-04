Variable is a label which helps to store data. To create a variable, we can assign it a value with the help of assignment operator. Based on the type of value assigning, the memory will dynamically allocate for the variable

Example:

    roll_number = 12345

    # roll_number is a variable
    # = is an assignment operator
    # 12345 is the value stored in roll_number variable

## **Rules for Variable Creation**

* **`Lowercase or uppercase or digits or underscore`** A Variable name can only contain lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_)
* **`No digit start`** A variable name cannot start with a digit (0 to 9)
* **`Lowercase and uppercase or underscore start`** 3. A variable name can start with a lowercase (a to z) or uppercase (A to Z) or an underscore (_)
* **`Case-Sensitive`** Variable name is case-sensitive (a = 5, A=6 -> a and A are two different variables in python)
* **`No Special Characters`** The variable name cannot have special characters such as !, @, #, $, % etc..

## **Multiple Assignment**
We can assign values to multiple variables in a single line like this a = b = c = 100

    #Multiple Assignment with single value
    a=b=c=100
    print(a, b, c)

    #Multiple Assignment with multiple value
    a, b, c = 10, 20, 30
    print(a, b, c)

 Output

    100 100 100
    10 20 30

## **Constants in Python**
Constant is a value that remains the same which cannot change or modify once it get declared. Python don't have constant declaration as like in Java. We can declare a variable or value as constant in Python and make sure which don't get the modification.

**`Rules`** - Constant variables should have only capital letters and underscores (for word separation)

    #Constant Example
    PI = 3.14
    print(PI)

 Output

    3.14