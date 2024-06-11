def d():
    print('='*75)

# Looping over tuples is the exact same as looping over lists

# we can write a function that loops over a given tuple

# EX 1
def tup_loop(atuple):

    for item in atuple:
        print(item)

my_tup = 'apple', 'banana', 'orange'

tup_loop(my_tup)

# EX 2
def while_tup(atuple):
    i = 0
    while i < len(atuple):
        print(atuple[i])
        i += 1

teams = 'Bull Dogs', 'Falcons', 'Hawks', 'Braves'

while_tup(teams)

d()

#-- enumerate() function : allows us to iterate over the index and item at the same time

today = 'woke up', 'ate breakfast', 'went to the gym', 'prepped for lecture', 'ate lunch', 'graded', 'meetings', 'in class'

# enumerate() : returns a tuple of each item and its index

for task in enumerate(today):
    print(task[1])
d()
for idx, task in enumerate(today):
    print(idx)
    print(task)