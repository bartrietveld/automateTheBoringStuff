def takeList(list):
    """ Takes a list value as an argument
    Returns a string with all the items separated by comma and space, wich and inserted before last item"""
    newString = ""

    if len(list) == 0: # Create an exception for empty lists
        print("This is an empty list.")
        return False

    elif len(list) == 1:
        return list[0]

    else:
        newString += list[0] # Add the first word from the list to the new string

        for i in range(1,len(list)-1): # Add comma and word for all words in list before last word
            newString += ", " + list[i]
        
        newString += ' and ' + list[len(list)-1] # Before last word, add 'and' and add last word
    
        return newString

# Test cases:
print('************* Evaluation of function *************',end='\n\n')

print(takeList([]),end='\n\n') # Empty list should evaluate to False

print(takeList(["Hello"]),end='\n\n') # List with one string should return only item in list

print(takeList(["Apple",'Bananas','Tomato','Egg']),end='\n\n') 

print(takeList(["Apple",'Bananas']),end='\n\n') 

print('**************************************************')




