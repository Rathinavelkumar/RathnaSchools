With the help of try, catch and finally statements, we can handle the exceptions in python programming. Lot of inbuilt exception are available in python which are raised if the program encounters an error 

## **Built-In  Exceptions**
Below are the list of inbuilt exception which occurs at runtime due to logical errors

| Exception | Reason for exception |
| :------------ |-----: |
| **Assertion Error** | occurs during the failure of assert statements |
| **Attribute Error** | occurs during the failure of attribute assignment |
| **EOF Error** | occurs when the input function reaches the end of file condition|
| **Floatingpoint Error** | occurs during the failure of floating point operations|
| **GeneratorExit Error** | occurs if the closed method is called in generator|
| **Import Error** | occurs if the imported module is not found|
| **KeyError Error** | occurs during the failure of founding key in given dict|
| **KeyInterrupt Error** | occurs if the console receives delete or ctrl+c commands|
| **Memory Error** | occurs if the memory exceeds the limit|
| **Name Error** | occurs if the variable is not available in the given scope|
| **NotImplemented Error** | occurs if the class not implemented the abstract methods|
| **OS Error** | occurs during the system related failures|
| **Overflow Error** | occurs during the failure to represent large arithmetic operation|
| **Reference Error** | occurs during the garbage collected referent access by a week reference proxy|
| **Runtime Error** | occurs during the occurrence of unidentified exception |
| **Stopiteration Error** | occurs when the iterator function not having any other items to iterate |
| **Syntax Error** | occurs during the error in program syntax|
| **Indentation Error** | occurs due to incorrect indentation|
| **Tab Error** | occurs due to inconsistent tabs or spaces in indentation|
| **System Error** | occurs due to the internal error faced by interpreter|
| **System Exit** | occurs due to sys.exit function|
| **Type Error** | occurs due to the incorrect object type|
| **Unboundlocal Error** | occurs due to the missing of value for the given variable in a function|
| **Unicode Error** | occurs due to the error in unicode related encoding and decoding|
| **UnicodeEncode Error** | occurs due to the error in unicode related encoding|
| **UnicodeDecode Error** | occurs due to the error in unicode related decoding|
| **UnicodeTranslate Error** | occurs due to the error in unicode related translating|
| **Value Error** | occurs due to the improper value for the passed arguments with correct type|
| **ZeroDivision Error** | occurs due to zero value in division or modulo operation's second operand|

## **Try and Except clause**
The major functionality which can raise exception should be declare inside try statement and the code which handles the raised exception should be declare inside the except clause like the below sample program

    #Exception Handling
    num1 = 10
    num2 = 0
    try:
        result = num1//num2
    except:
        print("Exception occurs during division operation")

 Output

    Exception during division operation

## **Try and Multiple Except clause**
Its not a good practice the exception in very general way like the above program. We should handle the exception based on the type of exception raises like the below programs

Program 1: Handling Zero Division Exception

    #Handling Zero Division Exception
    num1 = 10
    num2 = 0
    try:
        result = num1//num2
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer type objects")
    except Exception as E:
        print("Exception occurs during division operation")

 Output

    The second operand value shouldn't be zero of division operation

Program 2: Handling invalid type Exception

    #Handling invalid type Exception
    num1 = 10
    num2 = "0"
    try:
        result = num1//num2
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer objects")
    except Exception as E:
        print("Exception occurs during division operation")

 Output

    The division operation cannot be perform for non integer objects

Program 3: Handling General Exceptions

    #Handling general Exception
    num1 = 10
    try:
        result = num1//num2
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer objects")
    except Exception as E:
        print("Exception occurs during division operation")

 Output

    Exception occurs during division operation

## **Try, Except and Else clause**
After the successful execution of try statement, if we want to execute some other code that can be handle in else clause. If no exception occurs in execution, else clause block executes by the interpreter

    #Else clause
    num1 = 10
    num2 = 5
    try:
        result = num1//num2
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer objects")
    except Exception as E:
        print("Exception occurs during division operation")
    else:
        print(result)

 Output

    2

## **Try, Except and Finally clause**
Finally clause executes for both successful and exceptional cases. Usually it uses for cleanup the resources like the below program

Program 1: Finally clause - Successful scenario

    #Finally clause
    num1 = 10
    num2 = 2
    try:
        result = num1//num2
        print(result)
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer objects")
    except Exception as E:
        print("Exception occurs during division operation")
    finally:
        del num1
        del num2
        print("Finally clause Executed")

 Output

    5
    Finally clause Executed

Program 2: Finally clause - Exception scenario

    #Finally clause
    num1 = 10
    num2 = 0
    try:
        result = num1//num2
        print(result)
    except ZeroDivisionError:
        print("The second operand value shouldn't be zero of division operation")
    except TypeError:
        print("The division operation cannot be perform for non integer objects")
    except Exception as E:
        print("Exception occurs during division operation")
    finally:
        del num1
        del num2
        print("Finally clause Executed")

 Output

    The second operand value shouldn't be zero of division operation
    Finally clause Executed