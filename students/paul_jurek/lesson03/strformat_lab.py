"""module to solve string formatting lab for lesson 3"""
import pytest


# Task 1
"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
input = (2, 123.4567, 10000, 12345.67)
output = f'file_{input[0]:0=3} :   {input[1]:.2f}, {input[2]:.2E}, {input[3]:.3g}'
print(output)

# Task 2
# using standard format to compare with f-strings
output_format = 'file_{:0=3} :   {:.2f}, {:.2E}, {:.3g}'.format(input[0],
                                                                input[1],
                                                                input[2],
                                                                input[3])
print(output_format)


# task 3
def formatter(tup_input):
    """builds string to print out the numbers based off tuple input
    args:
        tup_input: vaiable length tuple with digit inputs
    returns:
        string stating number of items in tuple and listing them out
        this is output as variable"""

    template_str = 'the {} numbers are: '
    n = len(tup_input)
    fillin_str = ', '.join(['{}']*n)
    template_str += fillin_str

    return(template_str.format(n, *tup_input))


@pytest.mark.parametrize(['test_input', 'expected'], [
    ((1, 2, 3), 'the 3 numbers are: 1, 2, 3'),
    ((1, 2, 3, 4), 'the 4 numbers are: 1, 2, 3, 4'),
    ((1,), 'the 1 numbers are: 1'),
    ((), 'the 0 numbers are: ')
])
def test_formatter(test_input, expected):
    assert formatter(test_input) == expected


# task 4
"""Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions."""


def inside_out(tuple5):
    """funtion to re-order and print input
    args:
        tuple of length 5 containing strings.  Assume all strings and no input checking

    returns:
        str with output of 'tuple[3] tuple[4] tuple[2] tuple[0] tuple[1]' with formatting (see test)
        prints results to console"""

    output = f'{tuple5[3]:02} {tuple5[4]:02} {tuple5[2]:04} {tuple5[0]:02} {tuple5[1]:02}'
    print(output)
    return output


def test_inside_out():
    """Given a 5 element tuple:
        ( 4, 30, 2017, 2, 27)
        use string formating to print:
        '02 27 2017 04 30'
        Hint: use index numbers to specify positions."""
    input = (4, 30, 2017, 2, 27)
    assert inside_out(input) == '02 27 2017 04 30'


def format_fruit_list(fruits, uppercase=False, fat_fruit=False):
    """as part of task 5, this formats fruit lists
    ars:
        fruits: list of fruits which should be divisable by 2.
            first entry is fruit name and second is weight in some unit
            eg. ['oranges', 1.3, 'lemons', 1.1]
    returns
        string telling fruit name and weight
            eg. The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    for index, fruit in enumerate(fruits):
        if index % 2 == 0:
            name = fruits[index][:-1]
            name = name.upper() if uppercase else name

            weight = fruits[index+1]
            weight = weight * 1.2 if fat_fruit else weight

            if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                leader = 'an'
            else:
                leader = 'a'
            if index == 0:
                output = f'The weight of {leader} {name} is {weight}'
            else:
                output += f' and the weight of {leader} {name} is {weight}'
    return output


@pytest.mark.parametrize(['test_input', 'input_upper', 'input_big_fruit', 'expected'], [
    (['oranges', 1.3, 'lemons', 1.1], False, False, 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'),
    (['oranges', 1.3, 'lemons', 1.1], True, False,  'The weight of an ORANGE is 1.3 and the weight of a LEMON is 1.1'),
    (['oranges', 1.3, 'lemons', 1.1], False, True,  'The weight of an orange is 1.56 and the weight of a lemon is 1.32'),
    (['oranges', 1.3], False, False,  'The weight of an orange is 1.3'),
    (['oranges', 1.3, 'dragonfruits', 3, 'mangos', 2.5], False, False,  'The weight of an orange is 1.3 and the weight of a dragonfruit is 3 and the weight of a mango is 2.5'),
    ])
def test_format_fruit_list(test_input, input_upper, input_big_fruit, expected):
    """Here’s a task for you: Given the following four element list:
        ['oranges', 1.3, 'lemons', 1.1]
        Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1"""
    assert format_fruit_list(test_input, uppercase=input_upper, fat_fruit=input_big_fruit) == expected


def task6_table():
    """Write some Python code to print a table of several rows,
    each with a name, an age and a cost. Make sure some of the
    costs are in the hundreds and thousands to test your
    alignment specifiers.

    It is not clear in instructions but I am assuming task is
    to make decimal points line up in cost column"""
    data = (('Paul', 33, '$10000.00'), ('Cole', 5, '$200.00'), ('Dylan', 2, '$1.00'))
    for entry in data:
        print(f'{entry[0]:15} {entry[1]:>3} {entry[2]:>15}')


def task_6_extra_credit(tuple10, string_choice='f'):
    """And for an extra task, given a tuple with 10 consecutive
    numbers, can you work how to quickly print the tuple in
    columns that are 5 charaters wide? It’s easily done
    on one short line!"""
    [print(f'{i:5}', end=" ") for i in tuple10]
