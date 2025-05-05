Looping statements are used to execute the same instruction again and again until the conditions get satisfied

## **While Loop**
While loop not require any iterable, it will execute a block of code repeatedly until the condition get fails

    #While Loop
    count = 0

    #Looping for 5 times
    while count<5:
        print(count)
        #Increment is mandatory here, otherwise results in infinite loop
        count=count+1

 Output

    0
    1
    2
    3
    4

## **While Break**
Even though the condition is true still we can stop the loop with the help of break statement 

    #While Break Loop
    count = 0

    #Looping for 3 times
    while count<5:
        print(count)
        count=count+1
        #break the loop when count is 3
        if count==3:
            break

 Output

    0
    1
    2

## **While Continue**
Even though the condition is true still we can stop the specific iteration using continue statement 

    #While Continue
    count = 0

    #Looping for 4 times
    while count<5:
        count=count+1
        #skip the print when count is 3
        if count==3:
            continue
        print(count)

 Output

    1
    2
    4
    5

## **While Else**
One of the unique feature in python is while loop with else clause

    #While Else
    count = 0

    #Looping for 4 times
    while count<5:
        count=count+1
        print(count)
    else:
        print("Loop broken - count is higher than 5 now")

 Output

    1
    2
    3
    4
    5
    Loop broken - count is higher than 5 now

## **While Break Else**
One of the unique feature in python is while loop with else clause

    #While Break Else
    count = 0

    #Looping for 4 times
    while count<5:
        count=count+1
        if count==3:
            break
        print(count)
    #Else statement won't execute since loop breaks
    else:
        print("Loop broken - count is higher than 5 now")

 Output

    1
    2

## **While Continue Else**
Else statement execute for continue since it will only skip only the particular execution 

    #While Continue Else
    count = 0

    while count<5:
        count=count+1
        if count==3:
            continue
        print(count)
    #Else statement execute since loop continues
    else:
        print("Loop broken - count is higher than 5 now")

 Output

    1
    2
    4
    5
    Loop broken - count is higher than 5 now

