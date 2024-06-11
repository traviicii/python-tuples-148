def d():
    print('='*75)

# Tuple

#-- Tuples are a data type that are similar to lists, with the excepetion that they are immutable

#-- immutable : you cannot change or edit the data of a tuple, but we can reassign what is stored in a variable
#-- ordered : just like lists they have an order, we can access elements in a tuple by indexing
#-- like lists, tuples can store a variety of objects, any data type, including duplicate objects

# why bother?
# you can create a collection of data that connat be changed by you or any other developer you might work with
# iterating over a tuple is faster than iterating over a list


# we use () to define tuples, just like in lists we use [] empty_list = []
empty_tup = ()

# singleton, tuple with one item
singelton = ('element',) # requires a trailing comma

print(type(singelton))
print(singelton)

d()
# tuple with multiple elements inside
# with multiple element, you no longer require a trailing comma

pop_tup = ('this', 'is', 'a', 'populated', 'tuple')
print(type(pop_tup))
print(pop_tup)

variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) # can store just about anything
print(variety_tup)


duple = (True, True, True, False, False, False, True) # can have duplicate items as well
print(duple)

d()

# packing tuples

# we can pack tuples, without parenthesis
packed = 't-shirt', 'pants', 'jacket', 'socks'
print(type(packed))
print(packed)

# unpack into multiple variables if we like
tup_pack = pop_tup, variety_tup, duple
print(tup_pack)

d()
# Indexing and Slicing into tuples

pop_tup = ('this', 'is', 'a', 'populated', 'tuple')
print(pop_tup[3][4]) #looking at the 3rd index and then indexing into the string stored there to get what is stored at the 4th index
print(pop_tup[1])
print(pop_tup[1][1]) # the 's' in is

variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) # can store just about anything
print(variety_tup[3][0])

d()

# Slicing [start:stop] : default start = 0 and stop = end of the tuple
# if you specify a stop value, that stop stop value is non-inclusive

duple = (True, True, True, False, False, False, True)
print(duple[:3])

print(duple[1:4])

print(duple[3:6])

d()

historical_record = ('Medieval Era', ('Knights', 'Castles', ('King', "Queen")), 'Renaissance Period')
print(historical_record[1][2][1])