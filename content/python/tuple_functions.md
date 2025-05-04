Various built-in functions are available in Python which helps to perform multiple operations on tuple. Below are the top must know tuple methods in python

## **Count Method**
This function helps to returns the occurrence count of specified object in given tuple

    #Count Function
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    print("The count of 10 in the tuple is : {}".format(mark_list.count(10)))

 Output

    The count of 10 in the tuple is : 3

## **Index Method**
This function returns the index of first occurrence for the given value

    #Index Method
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    #Returns the index of first occurrence
    print("The index of 60 is : {}".format(mark_list.index(60)))

 Output

    The index of 60 is : 5


## **Max Function**
This function returns the maximum value of the given tuple 

    #Max Function
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    #Returns the maximum element in the given list
    print("The maximum element in the given tuple is : {}".format(max(mark_list)))

 Output

    The maximum element in the given list is : 60

## **Min Function**
This function returns the minimum value of given list 

    #Min Function
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    #Returns the minimum element in the given list
    print("The minimum element in the given tuple is : {}".format(min(mark_list)))

 Output

    The minimum element in the given tuple is : 10

## **Sum Function**
This function returns the summation of all the values in the given tuple

    #Sum Function
    month_list = (10, 20, 30, 40, 50)
    print("The sum of tuple is : {}".format(sum(month_list)))

 Output

    The sum of tuple is : 150

## **Length Function**
This function returns the total length of given list

    #length Function
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    print("The length of tuple is : {}".format(len(mark_list)))

 Output

    The length of tuple is : 8

## **Sort Function**
Sort Method returns the sorting order of the given tuple

    #Sort Function
    mark_list = (10, 20, 30, 10, 50, 60, 10, 60)
    print("Tuple before sorting : ")
    print(mark_list)

    print("Tuple after sorting - ascending : ")
    print(sorted(mark_list))

    print("Tuple after sorting - descending : ")
    print(sorted(mark_list, reverse=True))

 Output
    
    Tuple before sorting : 
    (10, 20, 30, 10, 50, 60, 10, 60)
    Tuple after sorting - ascending : 
    [10, 10, 10, 20, 30, 50, 60, 60]
    Tuple after sorting - descending : 
    [60, 60, 50, 30, 20, 10, 10, 10]