import os
import textwrap
import pickle

from scipy.weave.catalog import os_dependent_catalog_name


def create_todo(todos, title, description, level):
    todo = {
        'title': title,
        'description': description,
        'level': level
    }
    todos.append(todo)

def delete_todo(todos):
    pass


def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field + " > ")
    return user_input


def test(todos, abcd, ijkl):
    return "Command 'test' returned:\n" + \
        "abcd: " + abcd + "\nijkl: " + ijkl


def get_function(command_name):
    return commands[command_name][0]


def get_fields(command_name):
    return commands[command_name][1]


def run_command(user_input, data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "?" \
            " I don't know what that command is."
    else:
        the_func = get_function(user_input)

    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    return the_func(todos, **data)

def show_todo(todo, index):
    wrapped_title = textwrap.wrap(todo['title'], 16)
    wrapped_descr = textwrap.wrap(todo['description'], 24)

    output = str(index + 1).ljust(8) + "  "
    output += wrapped_title[0].ljust(16) + "  "
    output += wrapped_descr[0].ljust(24) + "  "
    output += todo['level'].ljust(16)
    output += "\n"

    max_len = max(len(wrapped_title),
                  len(wrapped_descr))
    for index in range(1, max_len):
        output += " " * 8 + "  "
        if index < len(wrapped_title):
            output += wrapped_title[index].ljust(16) + "  "
        else:
            output += " " * 16 + "  "
        if index < len(wrapped_descr):
            output += wrapped_descr[index].ljust(24) + "  "
        else:
            output += " " * 24 + "  "
        output += "\n"

    return output

def show_todos(todos):
    sorted_todos = sort_todos(todos)
    output = ("Item      Title             "
              "Description               Level\n")
    for index, todo in enumerate(sorted_todos):
        output += show_todo(todo, index)
    return output

def capitalize(todo):
    todo['level'] = todo['level'].upper()
    return todo

def sort_todos(todos):
    important_todos = [capitalize(todo) for todo in todos if todo['level'].lower() == 'important']
    medium_todos = [todo for todo in todos if todo['level'].lower() == "medium"]
    unimportant_todos = [todo for todo in todos if todo['level'].lower() not in ["important", "medium"]]
    sorted_todos = important_todos + medium_todos + unimportant_todos
    return sorted_todos

def save_todo_list(todos, filename='todos.pickle'):
    pickle.dump(todos, open(filename, 'wb'))

def load_todo_list(stuff, filename='todos.pickle'):
    global todos
    if filename in os.listdir('.'):
        todos = pickle.load(open(filename, 'rb'))
    else:
        return "The file " + filename + " does not exist!"

def main_loop():
    user_input = ""
    load_todo_list('blah')
    while 1:
        user_input = raw_input("> ")
        if user_input.lower().startswith("quit"):
            print "Exiting"
            break
        else:
            print run_command(user_input)
    save_todo_list(todos)


commands = {
    'new':  [create_todo, ['title', 'description', 'level']],
    'test': [test, ['abcd', 'ijkl']],
    'show': [show_todos, []],
    'save': [save_todo_list, []],
    'load': [load_todo_list, []]
}

todos = []



if __name__ == '__main__':
    main_loop()