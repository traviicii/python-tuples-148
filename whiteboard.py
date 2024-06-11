# Write a function that removes the spaces from the string, then return the resultant string.
# Your input will always be a string that only contains spaces, numbers, and letters.

# Examples:

# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"
# "                 " -> ""

# create a empty string to store characters that aren't empty spaces
# create a for loop that looks at each letter
# Maybe use a pass or continue statement if I come accross a character
    # add it to my empty



#.strip()

# new = astring.strip()
# return ''.join(astring)

#.replace()

# I'll just reassign the string given to the return value from the .replace() method
# astring.replace(" ", "")

# astring = "8 j 8   mBliB8g  imjB8B8  jl  B"

def solution(astring):
    return astring.replace(" ", "")

# this_string = "8 j 8   mBliB8g  imjB8B8  jl  B"
# new_string = ''

# for letter in this_string:
#     if letter == ' ':
#         continue
#     else:
#         new_string += letter

# print(new_string)