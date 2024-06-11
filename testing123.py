
test = {
    0 : 'first value in my dict',
    1 : 'second thing in the dictionary',
    2 : 'third thing'
}

print(test[1])

def keys_makr(some_crazy_thing):
    list_of_keys = []
    for i in some_crazy_thing.keys():
        list_of_keys.append(i)
    return list_of_keys

key_list = keys_makr(test)

print(test[0])

# print(test.keys())

# keys = test.keys()

# print(test)


print(test.items())
print(test.keys())
print(test.values())
print("------")
for key, val in enumerate(test):
    if key == 1:
        del test[key]
    print(key, val)