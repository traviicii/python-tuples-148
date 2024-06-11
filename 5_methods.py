def d():
    print('='*75)

# tuple methods

# tuples don't have many methods

#-- tuple.count(item) : counts how many times an items appears in a tuple

shopping = 'eggs', 'milk', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))

#-- len(tuple) : returns the lenght of the given tuple

print(len(shopping))

#-- tuple.index(item) : return the first index of that item

print(shopping.index('creamer'))
print(shopping.index('chicken'))


#-- membership checks of a tuple, if item in tuple, 'in', return True or False

print('creamer' in shopping)
print('Cinnamon Toast Crunch' in shopping)

nest = 'start', ('early', 'middle', 'towards end'), 'end'

for item in nest:
    if isinstance(item, tuple) and 'middle' in item:
        print('I found the middle!')