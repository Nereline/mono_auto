from helpers.db_simple_helper import get_templates_from_db
import pytest


def test_db(session, db_connect):
    try:
        db_connect.execute("select ...")
        row = db_connect.fetchone()
        if row:
            print(row)
    except:
        pytest.skip('Не удался коннект к бд')
