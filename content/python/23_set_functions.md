Various built-in functions are available in Python which helps to perform multiple operations on sets. Below are the top must know set methods in python

## **Length Function**
This function helps to return the length of the given set 

    #Length Method
    month_list = {"Jan", "Feb", "Mar", "Apr", "May"}
    print("Length of given set is: {}".format(len(month_list)))

 Output

    Length of given set is: 5

## **Set Union**
This helps to returns the union results of two sets

    #Set Union
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Apr"}
    print("The union result of given two sets are")
    print(month_list_old | month_list_new)

 Output

    The union result of given two sets are
    {'Apr', 'Feb', 'Mar', 'Jan'}

## **Set Intersection**
This helps to return the intersection results of given sets

    #Set Intersection
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Apr"}
    print("The intersection result of given two sets are")
    print(month_list_old & month_list_new)

 Output

    The intersection result of given two sets are
    {'Jan', 'Feb'}

## **Set Difference**
This helps to return the set difference of one set from another set

    #Set Difference
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Apr"}
    print("The set difference of one set from another set is")
    print(month_list_old - month_list_new)

 Output

    The set difference of one set from another set is
    {'Mar'}

## **Set symmetric Difference**
This return the element which is available in any one of the given set. If it is available in both set, it won't return as result

    #Set Symmetric Difference
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Apr"}
    print("The set symmetric difference is :")
    print(month_list_old ^ month_list_new)

 Output

    The set symmetric difference is :
    {'Mar', 'Apr'}

## **Clear Method**
This method removes all the element in given set and make it as empty set

    #Clear Set Method
    month_list = {"Jan", "Feb", "Mar"}

    month_list.clear()
    print("The clear set result is :")
    print(month_list)

 Output

    The clear set result is :
    set()

## **Pop Method**
This method helps the remove the random value from the given set

    #POP Method
    month_list = {"Jan", "Feb", "Mar"}

    month_list.pop()
    print("The POP method removes random value :")
    print(month_list)

 Output

    The POP method removes random value :
    {'Jan', 'Feb'}

Note: Since POP method removes value randomly from given set, you may end up in different output

## **Isdisjoint Method**
This method returns true if both sets not have any common element

    #Isdisjoint Method
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Apr", "May", "Jun"}

    print("Isdisjoint method result is :")
    print(month_list_old.isdisjoint(month_list_new))

 Output

    Isdisjoint method result is :
    True

## **Issubset Method**
This method returns true if all element of given set is present in the another set

    #Issubset Method
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Mar", "Apr", "May", "Jun"}

    print("Issubset method result is :")
    print(month_list_old.issubset(month_list_new))

 Output

    Issubset method result is :
    True

## **Issuperset Method**
This method returns true if the given set have all the element of another set

    #Issuperset Method
    month_list_old = {"Jan", "Feb", "Mar"}
    month_list_new = {"Jan", "Feb", "Mar", "Apr", "May", "Jun"}

    #Return False - only 3 elements are present, remaining items missed
    print(month_list_old.issuperset(month_list_new))

    #Return True - all items are present in month_list_new
    print(month_list_new.issuperset(month_list_old))

 Output

    False
    True