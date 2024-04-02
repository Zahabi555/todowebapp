def get_todos(filepath=r"C:\Users\ramiz\PycharmProjects\todowebapp\todos.txt"):# todos.txt is default now
    """
    This function reads a file and returns a list of to-do items
    """

    with open(filepath, 'r',encoding='utf-8') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(string, filepath=r"C:\Users\ramiz\PycharmProjects\todowebapp\todos.txt"):
    with open(filepath, 'w',encoding='utf-8') as file:
        todos_local = file.writelines(string)

