"""Reorder sequences using slicing only"""

import copy
#I am intentionally using copy instead of sequence_copy = sequence[:]
#because I don't like the shallow copy behavior that allows changing
#elements in a list of lists to effect the original
#I want to get in the habit of using copy remembering that this can happen

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_last_first(sequence):
    """Reorder sequence switching the first and last elements"""
    new_sequence = copy.copy(sequence)
    first = new_sequence[:1]
    last = new_sequence[-1:]
    center = new_sequence[1:-1]
    return last+center+first

def skip_every_other(sequence):
    """Remove every other element in the sequence"""
    new_sequence = copy.copy(sequence)
    return new_sequence[::2]



def tests():
    """Test the ________ functions"""
    assert exchange_last_first(a_string) == "ghis is a strint"
    assert exchange_last_first(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert skip_every_other(a_string) == "ti sasrn"
    assert skip_every_other(a_tuple) == (2, 13, 5)
    #assert mid_last_first(a_string) == "is a stringthis "
    #assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)

if __name__ == "__main__":
    tests()
    print('Lesson3: Slicing Exercise')
    print(f'LessonX: _______ Exercise - {exchange_last_first.__doc__}')
    print(f'{a_string} becomes {exchange_last_first(a_string)}')
    print(f'{a_tuple} becomes {exchange_last_first(a_tuple)}')
    print('')
    print(f'LessonX: _______ Exercise - {skip_every_other.__doc__}')
    print(f'{a_string} becomes {skip_every_other(a_string)}')
    print(f'{a_tuple} becomes {skip_every_other(a_tuple)}')
    print('')
