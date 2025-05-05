Similar to while loop, for loops are also used to execute the same instruction again and again until the conditions get satisfied and also helps to iterating list sequence, tuple sequence etc.

## **For Loop**
There are two use cases available for **FOR** loop statement in python

`First Use Case` - Iterating over the sequence data types without any specific index variable

    #For Loop - Without Index
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for each_month in month_list:
        print(each_month)

 Output

    Jan
    Feb
    Mar
    Apr
    May

`Second Use Case` - Iterating with specified number of times - Using Range Function

    #For Loop - With Index
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        print(month_list[index])

 Output

    Jan
    Feb
    Mar
    Apr
    May

## **For Break**
Even though the condition is true still we can stop the loop with the help of break statement 

    #For Break
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        if month_list[index]=="Apr":
            break
        print(month_list[index])

 Output

    Jan
    Feb
    Mar

## **For Continue**
Even though the condition is true still we can stop the specific iteration using continue statement 

    #For Continue
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        #only skip April month
        if month_list[index]=="Apr":
            continue
        print(month_list[index])

 Output

    Jan
    Feb
    Mar
    May

## **For Else**
One of the unique feature in python is for loop with else clause. When the condition get false it will execute the else statement 

    #For Else
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        print(month_list[index])
    else:
        print("I am else block")

 Output

    Jan
    Feb
    Mar
    Apr
    May
    I am else block

## **For Break Else**
When break is executed, the else wont execute in for loop 

    #For Break Else
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        print(month_list[index])
        if month_list[index]=="Mar":
            break
    #Else block wont execute since it breaks
    else:
        print("I am else block")

 Output

    Jan
    Feb
    Mar

## **For Continue Else**
Else statement execute for continue since it will only skip only the particular execution

    #For Continue Else
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]

    for index in range(0, len(month_list)):
        if month_list[index]=="Mar":
            continue
        print(month_list[index])
    #Else block execute since it continues
    else:
        print("I am else block")

 Output

    Jan
    Feb
    Apr
    May
    I am else block

