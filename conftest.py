import pytest
import pyodbc
from models.session_constructor import Session


@pytest.fixture(scope="session")
def session():
    session = Session()
    session.create_session()
    return session


