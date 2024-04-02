import os

current_dir = os.path.dirname(os.path.abspath(__file__))

default_filepath = os.path.join(current_dir, "todos.txt")



def get_todos(filepath=default_filepath):# todos.txt is default now
    """
    This function reads a file and returns a list of to-do items
    """

    with open(filepath, 'r',encoding='utf-8') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(string, filepath=default_filepath):
    with open(filepath, 'w',encoding='utf-8') as file:
        todos_local = file.writelines(string)

