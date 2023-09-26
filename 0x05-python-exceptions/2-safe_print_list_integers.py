#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print the first x elements of a list that are integers.

    Args:
        my_list (list): the list to be printed elements from.
        x (int): the number of elements of my_list to be printed.

    Returns:
        number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
