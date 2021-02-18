import models.http as http
from data.endpoints import depositrateinfo
from models.session_constructor import Headers


def deposit_rateinfo(session):
    resp = http.parametrized_get(host=session['host'],
                                 endpoint=depositrateinfo,
                                 header_payload=Headers.default_header(session))
    return resp
