""" str.format = optional  method that gives users more control
                 when displaying output"""

animal = "cow"
item = "mo0on"

"""print(The 'animal' jumped over the 'moon')"""

print("The {} jumped over the {}".format("cow","moon")) #using plain strings
print("The {} jumped over the {}".format(animal,item)) #using variables 
print("The {1} jumped over the {0}".format(animal,item)) #using positional arguments
print("The {animal} jumped over the {item}".format(animal="dove",item="purse")) #using keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal,item))                 