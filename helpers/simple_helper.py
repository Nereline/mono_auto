import models.http as http
from data.endpoints import depositrateinfo


def deposit_rateinfo(session):
    resp = http.parametrized_get(host=session['host'],
                                 endpoint=depositrateinfo,
                                 header_payload={'DeviceToken': session['devicetoken'],
                                                 'SessionToken': session['sessiontoken'],
                                                 'Content-Type': r'application/json'})
    return resp
