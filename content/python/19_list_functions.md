Various built-in functions are available in Python which helps to perform multiple operations on list. Below are the top must know list methods in python

## **Append Method**
This function helps to add a new element to the given list

    #Append Method
    month_list = ["Jan", "Feb", "Mar", "Apr", "May"]
    print("List of element before appending: ")
    print(month_list)

    month_list.append("Jun")
    print("List of element after appending: ")
    print(month_list)

 Output

    List of element before appending: 
    ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    List of element after appending: 
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

## **Insert Method**
This function helps to add a new element at specified index to the given list

    #Insert Method
    month_list = ["Jan", "Feb", "Apr", "May", "Jun"]
    print("List of element before inserting: ")
    print(month_list)

    month_list.insert(2, "Mar")
    print("List of element after inserting: ")
    print(month_list)

 Output

    List of element before inserting: 
    ['Jan', 'Feb', 'Apr', 'May', 'Jun']
    List of element after inserting: 
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

## **Extend Method**
This function helps to extend another new list elements to the given list elements

    #Extend Method
    month_list = ["Jan", "Feb", "Mar"]
    month_list_new = ["Apr", "May", "Jun"]

    month_list.extend(month_list_new)
    print("List of element after appending: ")
    print(month_list)

 Output

    List of element after appending: 
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

## **Clear Method**
This function helps to clear all the element in the given list

    #Clear Method
    month_list = ["Jan", "Feb", "Mar"]
    print("List of element before clearance: ")
    print(month_list)

    month_list.clear()
    print("List of element after clearance: ")
    print(month_list)

 Output

    List of element before clearance: 
    ['Jan', 'Feb', 'Mar']
    List of element after clearance: 
    []

## **Pop Method**
This function helps to pop item at the specified index in the given list 

    #Pop Method
    month_list = ["Jan", "Feb", "Mar", "Dec", "Apr", "May", "Jun"]
    print("List of element before pop method: ")
    print(month_list)

    month_list.pop(3)
    print("List of element after pop method: ")
    print(month_list)

 Output

    List of element before pop method: 
    ['Jan', 'Feb', 'Mar', 'Dec', 'Apr', 'May', 'Jun']
    List of element after pop method: 
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

## **Sum Function**
This function returns the summation of all the values in the given list

    #Sum Function
    month_list = [10, 20, 30, 40, 50]
    print("The sum of list is : {}".format(sum(month_list)))

 Output

    The sum of list is : 150

## **Count Method**
This function returns the total occurrence of given value in the given list

    #Count Function
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    print("The count of 10 in the list is : {}".format(mark_list.count(10)))

 Output

    The count of 10 in the list is : 3

## **Length Function**
This function returns the total length of given list

    #length Function
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    print("The length of list is : {}".format(len(mark_list)))

 Output

    The length of list is : 8

## **Index Method**
This function returns the index of first occurrence for the given value

    #Index Method
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    #Returns the index of first occurrence
    print("The index of 60 is : {}".format(mark_list.index(60)))

 Output

    The index of 60 is : 5

## **Min Function**
This function returns the minimum value of given list 

    #Min Function
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    #Returns the minimum element in the given list
    print("The minimum element in the given list is : {}".format(min(mark_list)))

 Output

    The minimum element in the given list is : 10

## **Max Function**
This function returns the maximum value of the given list 

    #Max Function
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    #Returns the maximum element in the given list
    print("The maximum element in the given list is : {}".format(max(mark_list)))

 Output

    The maximum element in the given list is : 60

## **Sort Method**
Sort Method returns the sorting order of the given list

    #Sort Function
    mark_list = [10, 20, 30, 10, 50, 60, 10, 60]
    print("List before sorting : ")
    print(mark_list)

    mark_list.sort()
    print("List after sorting - ascending : ")
    print(mark_list)

    mark_list.sort(reverse=True)
    print("List after sorting - descending : ")
    print(mark_list)

 Output

    List before sorting : 
    [10, 20, 30, 10, 50, 60, 10, 60]
    List after sorting - ascending : 
    [10, 10, 10, 20, 30, 50, 60, 60]
    List after sorting - descending : 
    [60, 60, 50, 30, 20, 10, 10, 10]