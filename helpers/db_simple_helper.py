from models.session_constructor import DbConnect


def get_templates_from_db():
    connect = DbConnect()
    cursor = connect.db_connect()
    cursor.execute("select top(10) * from Templates")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()
