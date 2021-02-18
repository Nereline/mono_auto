import pytest
import pyodbc
from models.session_constructor import Session


@pytest.fixture(scope="session")
def session():
    session = Session()
    session.create_session()
    return session


@pytest.fixture(scope="session")
def db_connect():
    server = 'T-tdabb1-cdl01.abb-win.akbars.ru'
    database = ''
    username = ''
    password = ''
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()


