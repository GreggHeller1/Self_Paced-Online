#!/usr/bin/env python3
"""Demonstrate the ins and outs of Python lists"""
import copy

def fruits_list():
    """Create a list that contains Apples, “Pears, Oranges and Peaches"""
    return ['Apples', 'Pears', 'Oranges', 'Peaches']

def append_input_fruit():
    """Ask the user for another fruit and add it to the end of the list"""
    fruits = fruits_list()
    fruit_in = input("Please enter a new fruit: ")
    fruits.append(fruit_in)
    return fruits

def index_input_fruit(fruits):
    """Ask the user for a number, N, and return the Nth fruit in fruits_list"""
    try:
        num_in = int(input("Please enter a number: "))
        try:
            fruit = fruits[num_in-1]
        except IndexError as E:
            print('There aren\'t that many fruits')
            fruit = index_input_fruit(fruits)
    except ValueError as E:
        print('Thats not a number')
        fruit = index_input_fruit(fruits)
    return fruit

def add_fruit_plus(fruits):
    """Add another fruit to the beginning of the list using “+” """
    return ["Bananas"]+fruits

def add_fruit_insert(fruits):
    """Add another fruit to the beginning of the list using insert()"""
    fruits.insert(0,'Lemons')
    return fruits

def p_fruits(fruits):
    """Return all the fruits that begin with “P”, using a for loop."""
    p_fruits = []
    for fruit in fruits:
        if fruit[0].lower() == 'p':
            p_fruits.append(fruit)
    return p_fruits

def remove_last_fruit(fruits):
    """Remove the last fruit from the list."""
    del fruits[-1]
    return fruits

def remove_input_fruit(fruits):
    """Ask the user for a fruit to delete, find it and delete it.

    Bonus: Multiply the list times two.
    Keep asking until a match is found.
    Once found, delete all occurrences."""
    del_fruit = input("Please enter a fruit to delete: ")
    if del_fruit in fruits:
        while del_fruit in fruits:
            fruits.remove(del_fruit)
    else:
        print('That fruit isn\'t int the list')
        fruits = remove_input_fruit(fruits*2)
    return fruits



def tests():
    """Test the ________ functions"""
    pass

def exercise_demo(func_in, arg_in = None):
    """Print the lesson, exercise and task before demonstrating completion"""
    print(f'Lesson3: Series Exercise - {func_in.__doc__}')
    if arg_in is not None:
        my_list = func_in(arg_in)
    else:
        my_list = func_in()
    print(my_list)
    print('')
    return my_list

if __name__ == "__main__":
    tests()
    print('LessonX: _______ Exercise, Series 1')
    exercise_demo(fruits_list)
    fruits = exercise_demo(append_input_fruit)
    exercise_demo(index_input_fruit, arg_in = fruits)
    fruits = exercise_demo(add_fruit_plus, arg_in = fruits)
    fruits = exercise_demo(add_fruit_insert, arg_in = fruits)
    p_fruits = exercise_demo(p_fruits, arg_in = fruits)
    print('LessonX: _______ Exercise, Series 2')
    fruits1 = copy.copy(fruits)
    print(fruits1)
    #Hmm I just realized that returning the output is redundant since I never actually cpy the list...its always the same list
    #but funtions are still supposed to return things, so its not hurting anything?
    #nevrmind, we aactually do want to copy it so we can use it again later in series 3
    fruits2 = exercise_demo(remove_last_fruit, arg_in = fruits1)
    fruits2 = exercise_demo(remove_input_fruit, arg_in = fruits1)
