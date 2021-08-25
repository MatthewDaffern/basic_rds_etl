import pyodbc
import os


def grab_os_secrets(config_object):
    config_object['db_server'] = os.environ.get('db_server')
    config_object['db_db'] = os.environ.get('db_db')
    config_object['db_uid'] = os.environ.get('db_uid')
    config_object['db_pwd'] = os.environ.get('db_pwd')
    return config_object


def create_database_object(config):
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + config['db_server'] +
        ';DATABASE=' + config['db_db'] +
        ';UID=' + config['db_uid'] +
        ';PWD=' + config['db_pwd'])


def commit_rows(database_object, rows):
    """commits the rows"""
    for i in rows:
        cursor = database_object.cursor
        cursor.execute(i)
    cursor.commit()
    return 'committed data'


