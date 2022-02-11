
"""
    Types you can format Pyrhon printing data
"""
My_Country ="My country Name (SOMALIA)"
My_City="My Country City is (MUGDISHO)"
    #One #Normal print
print(My_City)
    #Two unsing Format (This format is Old way)
# default arguments
print("{}".format(My_Country))
print("{} , {}".format(My_City,My_Country))
# positional arguments
print("{0} , {1}".format(My_City,My_Country)) #Also yuo can use as Index
#keyword arguments
print("{My_Country} , {My_City}".format(My_Country="SOMALIA",My_City="MUGDISHO"))
# mixed arguments
print("{0} , {My_City}".format("SOMALIA",My_City="MUGDISHO" ))

# define Person dictionary
person = {'age': 30, 'name': 'Caaqil',"Gender":"male","tel":"612044116"}

# format
    # (**kwargs) is known as kwargs 
print("My name is :{name} , age is: {age} , My Gender {Gender} and My tell is {tel} ".format(**person))

    # unsing This Format
print(f"{My_City} , {My_Country}")

        #Three
    # %s placeholder //This formate was Python 2
    
print(" %s and  %s " % (My_Country,My_City,))





    

