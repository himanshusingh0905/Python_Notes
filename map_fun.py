# map() :  *  It returns a map object (an iterator). 
#          *  Basically this map() takes an iterable and a function/lambda and applies function to the 
#             each item of iterable. 

# Syntax of map() :   map(fun, iter)
#             Here,
#                    *   fun = A function to which map passes each element of given iterable.  
#                    *   iter = iterable( list, tuple, set, etc)

#--------------------------------------------------------------------------------------------------------------------------------

# Example:
# to double the value of each item of list
def add(n):
    return n + n

List = [2,3,11,12,23,24]
ans = map(add,List)
print(type(ans)) #  Output : <class 'map'>    (a map object)

# If I print it directly:
# print(ans)  # Yes, It prints but an address. like  ' <map object at 0x0000021B7B3AAA70> '

# Now to print items, we can convert it into other iterables like (list, tuple, set, unpackaging(using *) etc )
print(list(ans)) # prints list
# Note:
print(* ans) # prints nothing, bcz iterators are consumed ones and you've already consumed it in previous print statement. 

#--------------------------------------------------------------------------------------------------------------------------------
