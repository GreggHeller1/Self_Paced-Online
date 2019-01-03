#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

try:#
    joke = fun(first_try[0])
except NameError:
    # fun(first_try['spam']) ==> NameError: name 's' is not defined in except_test.py
    print("\nWhoops! there is no joke for: spam")
else:
    # 'Spam, Spam, Spam, Spam, Beautiful Spam' will only print if ther's no except,
    # but there is a NameError so joke = fun(first_try[1]) is never called
    joke = fun(first_try[1])

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
    # fun(first_try[2]) returns a string
except SyntaxError:
    # no SyntaxError occurs so continue to else
    print('Run Away!')
else:
    # not_joke holds the string, print it
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])  #  more_fun(langs[n]) returns nothing
except IndexError:
    pass
    # print("\nWhoops! index 5 is way out of index in the list [1, 2, 3]\n")
finally:
    # since above IndexError occurred, to continue using the same try - except block
    # finally:, what is executed disregarding whatever else happend has to be used
    more_joke = more_fun(langs[1])  #  more_fun(langs[n]) returns nothing
    last_fun()
