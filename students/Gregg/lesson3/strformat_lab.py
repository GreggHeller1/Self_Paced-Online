#!/usr/bin/env python3

"""Demonstrate pythons string formatting features"""

tupl = (2, 123.4567, 10000, 12345.67)
task_one = "file_{:03d}: {:.2f}, {:.2E}, {:03.2E}".format

def file_string(tupl):
    """Format the tuple into a string as in task 1 using an f string"""
    file_string = f"file_{str(tupl[0]).zfill(3)}: {tupl[1]:.2f}, {tupl[2]:.2E}, {tupl[3]:03.2E}"
    return file_string

def tests():
    """Test the ________ functions"""
    pass

if __name__ == "__main__":
    tests()
    print('Lesson3: String Formatting Exercise')
    print('Lesson3: Task One')
    print(task_one(*tupl))
    print('')
    print('Lesson3: Task Two')
    print(file_string(tupl))

