from helpers.simple_helper import deposit_rateinfo


def test_simple(session):
    resp = deposit_rateinfo(session.session_atr)
    print(resp)


