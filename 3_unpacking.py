def d():
    print('='*75)

# unpacking tuples reminder

packed = 'bacon', 'lettuce', 'tomato'
print(packed)

# basic unpacking

first, second, third = packed

print(first)
print(second)
print(third)

# will throw a Valuerror if the variables and items are not equal in number
#-- too many values to unpack, not enough variables
#-- too many variables, with not enough dat to unpack into them

# extended unpacking : *var takes additional data (data without a specified variable) and packs it into a list

enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everything bagel seasoning'
print(enhanced_blt)
d()

first, second, third, *condiments = enhanced_blt
print(first)
print(second)
print(third)
print(condiments)
d()

story = 'intro', 'conflict', 'builup', 'big reveal', 'climax', 'conclusion'
beginning, fight, *middle, end = story
print(beginning)
print(tuple(middle))

print(end)
print(fight)

# you can't have multiple * expressions or you'll get a SyntaxError