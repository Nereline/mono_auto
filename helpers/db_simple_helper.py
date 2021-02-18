import models.http as http
from models.session_constructor import Headers, DbConnect


def get_templates_from_db(session):
    connect = DbConnect()
    cursor = connect.db_connect()
    cursor.execute("SELECT...")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()
