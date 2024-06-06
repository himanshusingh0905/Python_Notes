# print( type(globals() ))     #  <class 'dict'>
# print( type(locals() ))      #  <class 'dict'>

print( globals() )
x = "David"
print( globals() ) # When you print this time, you would see {'x':'David'} is been added into the global namespace.

# Let's check if above x and 'x in dictionary' are same.
print( x is globals()['x']) # True

# Adding new value into that dictionary explicitly
globals()['y'] = 45
# Now accessing the same 
print(y) # Output : 45

#---------------------------------------------------------------------------------------------------------------------------

def fun():
    a = 96
    print(locals()) # {'a': 96}

fun()





