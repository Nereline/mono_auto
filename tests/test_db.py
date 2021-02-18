from helpers.db_simple_helper import get_templates_from_db
import pytest


def test_db(session, db_connect):
    if not db_connect:
        pytest.skip('Не удался коннект к бд')

    get_templates_from_db(session)
