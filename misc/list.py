# By using the slicing syntax change the following collections.

# After slicing:

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
# ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
# 'Hello World Huston we are here' -> 'World Huston we'
# Figure out more on your own and practice this a lot!

# Ex 1: Build-in functions on lists
# Look at this list of pythons build in functions.
# Try all of these in the interpretor (on a list you create). e.g len(a)
# Not all will work on lists, but try it out and see what works.
# Ex 2: Sort a Text
# Solution
l = []

def sort_list(x):
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']:
            l.append(i)
            l.sort()
    return print(l)

sort_list('hello world')
# Create a function that takes a string as a parameter and returns a list.

# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

# Ex 3: Sort a list
# Solution

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])

# Sort this list by using the sorted() build in function.

# Sort the list in reversed order.

# Sort the list on the lenght of the name.

# Sort the list based on the last letter in the name.

# Sort the list with the names where the letter ‘a’ is in the name first.

# Ex 4: Files
# Solution

# Create a file and call it lyrics.txt (it does not need to have any content)

# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

# open and read the content and write it to your terminal window. * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

# Ex 5: Sort a list of tuples
# Solution

# 1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
t = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

sorted(t, )

# 2. Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]