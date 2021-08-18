

def drop_capitalization(string_input):
    return string_input.lower()


def drop_end_spaces(string_input):
    return string_input.rstrip(' ').lstrip(' ')


def fold(var, funclist):
    for i in funclist:
        var = i(var)
    return var


def etl_func_list():
    return [drop_capitalization, drop_end_spaces]


def etl(string_input):
    return fold(string_input)

