#!/usr/bin/python3
'''
function that search and update
'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts new_string to a file, after find containing search_string'''
    with open(filename, "r+") as file:
        lines = file.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        file.seek(0)
        file.write("".join(changed))
