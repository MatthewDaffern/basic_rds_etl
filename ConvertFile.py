import pandas as pd


def grok_workbook(workbook_name):
    df = pd.read_excel(workbook_name, index_col=0)
    return df.values.tolist()


def grok_csv(csv_name):
    with open(csv_name, 'r+') as csv:
        return list(map(lambda x: x.split(','), csv.readlines()))


def if_csv(file_name):
    if 'csv' in file_name:
        return grok_csv(file_name)
    else:
        return file_name


def if_workbook(workbook_name):
    if 'xlsx' in workbook_name:
        return grok_workbook(workbook_name)
    else:
        return workbook_name


# convert them to a query ready format.

def inserter_converter(list_input):
    query_string = "INSERT INTO table_name(" + str.join(",", list_input[0]) + ")\n" + "VALUES\n"
    listy = list_input.pop(0)
    for i in listy:
        query_string = query_string + '(' + str.join(', ', i) + ')' + '\n'
    return query_string


def convert(file_name):
    return inserter_converter(if_csv(if_workbook(file_name)))
