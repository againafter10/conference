
"""
common test cases

"""




from constants import *


#################################
#################################


def check_input_argument():
    """
    :param: None
    :return: None

    Check if a file name is given as an input when invoking the module

    """
    print error[2]
    quit()


##################################
##################################

def check_input_file(fname):
    """
    :param fname: input filename
    :return: True or False

    check if the specified filename exists and is not empty

    """
    try:
        f = open(fname, 'r')
    except IOError:
        print error[0].format(fname)
        return False

    contents = f.read()
    f.close()

    if not contents:
        print error[1]
        return False

    return True


###################################
###################################


def check_talk_time(time):
    """
    :param time: talk time
    :return:
        True : if time numeric and time <=60
        False
    """
    if time > max_talk_time or type(time) != int:
        return False
    return True


###################################
###################################


def check_title_alphnumeric_null(title):
    """

    :param title: talk topic
    :return: True or False

    check if the talk topic is alphanumeric or blank
    """
    flag=False
    if title ==  '' :
        return True

    for i in title:
        if i.isdigit():
            return True
    return False

###################################
###################################


