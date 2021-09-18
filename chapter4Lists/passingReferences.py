""" Since in functions, reference to variable is passed, mutations done within the list to the parameter effects the variable outside the function """
def eggs(someParameter): 
    someParameter.append("Hello")

spam = [1,2,3]
eggs(spam)
print(spam)