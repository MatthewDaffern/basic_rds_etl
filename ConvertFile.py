from openpyxl import load_workbook


def grok_workbook(workbook_name):
    wb = load_workbook(filename=workbook_name)
    ws1 = wb.active
    # need to finish this. Gosh dynamic XLSX conversion sucks

def grok_csv(csv_name):
    #TODO

def if_csv(file_name):
    if 'csv' in file_name:
        return grok_csv(file_name)
    else:
        return file_name

def if_workbook(workbook_name):
    if 'xlsx' in workbook_name:
        return grok_workbook(workbook_name)
    else:
        return  workbook_name


def convert(file_name):
    return if_csv(if_workbook(file_name))
