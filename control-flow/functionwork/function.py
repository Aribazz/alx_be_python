# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#     print("Turn_right")

# turn_right()

# List
my_list = ["build", "work" , "execute"]
print(my_list)
print(my_list[1])



# Dictionary 
my_dictionary =  {"key": 1 , "name" : "Ariyo"}
print(type(my_dictionary))
print(my_dictionary["key"])

# FOR SEARCHING OF KEY IN A DICTIONARY
def funct(d,v):
    for key in d:
        if d[key] == v:
            return key
    return my_search

my_search = {"keyOne" : 1, "keyTwo" : 2 , "keyThree" : 3}
print(funct(my_search , 1))
# ////////////////////////////////////////

# FOR ITERATION 
my_list_iteration = [1,2,3,4,5,"name",True]
for item in my_list_iteration:
    print(my_list_iteration)

del my_list_iteration[5]
print(my_list_iteration)

# /////////////////////////////////////////

# DICTIONARY
student = {"name" : "Ariyo" , "age" : 29 }
del student["name"]
print(student)
# /////////////////////////////////

# Variable scope 
# count = 10

# def localCount ():
#     count = 5
#     print(f"local function : {count}")

#     def innerCount ():
#         count = 2
#         print(f"inner function : {count}")

#     innerCount()


# localCount()

# print(f"Global function : {count}")

# LEGB

# X = "Global x"

# def localVariable (z):
#     # global y
#     y = "Local Y"
#     print(z)

# localVariable("Global Z")
# print(y)

# Enclosing global scope with in inner function 

def outer ():
    x = "Global scope"

    def local ():
        nonlocal x
        x= "inner function"
        print(x)
    local()
    print(x)
outer()
# ////////////////////////////

# built in function and variable
# import builtins
# print(dir(builtins))

# # OOP
# class sheep:
#     def __init__(self, name , color):
#         self.name = name
#         self.color = color
#     def species(self):
#         print(f"This {self.color} is the unique one among multitude.")


# goat1 = sheep("BlackGoat" , "brown")
# goat2 = sheep("BlackBrownGoat" , "golden")

# print(goat1.species())
# ///////////////////////////////////////////////////////////////////////////

# RAISE 
# def divide (x,y):
#     if y == 0 :
#         raise ZeroDivisionError("Division by zero is not allowed")
#         return x / y


# print(divide())

#Sample inventory
purchase_inventory ={
    "apple" : 15,
    "orange": 10,
    "waterlemon": 5,
    "banana": 3
}

def purchase_details(item,quantity):
    try:
        if purchase_inventory[item] == 0:
            rasie ZeroDivisionError(item)
            else:

 




