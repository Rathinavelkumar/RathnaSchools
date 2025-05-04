keywords which should not used as any identifier, they are already reserved for special purposes by python interpreter

Below are the list of keywords in python (they are case - sensitive)

## **List of Keywords**

    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield

## **IsKeyword Method**
This function helps to check whether the given name is keyword or not

    #IsKeyword Method
    import keyword

    #Check with keywords in python
    print("'IS' a keyword in python? : {}".format(keyword.iskeyword("is")))
    print("'IN' a keyword in python? : {}".format(keyword.iskeyword("in")))

    #Check with Non-keywords in python
    print("'Rathna' a keyword in python? : {}".format(keyword.iskeyword("Rathna")))
    print("'Schools' a keyword in python? : {}".format(keyword.iskeyword("Schools")))

## **Kwlist Method**
Kwlist method helps to return the list of keywords available in python

    #kwlist Function
    import keyword

    #Check with keywords in python
    print(keyword.kwlist)

 Output

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']