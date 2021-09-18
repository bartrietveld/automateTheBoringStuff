""" Variables store values through id's
Lists are mutable. Multiple 
Strings and tuples imutable """

list = [1,2,3,4,5]
list2 = list
print(id(list))
print(id(list2))

string = "Hello"
string2 = string

print(id(string))
print(id(string2))

string += "World"
# What happens here is that the value in string can't be changed, since strings are imutable. So a new string is created on a new memory location. 
print(id(string))
print(id(string2))
