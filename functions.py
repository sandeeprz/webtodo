FILEPATH = 'file.txt'
def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


