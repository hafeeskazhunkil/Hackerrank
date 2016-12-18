"""
Read a line of input from stdin and save it to a variable, . Then print the contents of  to stdout.
"""
def read():
    s = raw_input()
    return s


if __name__ == '__main__':
    my_str = read()
    print my_str
