from data.users import said
import models.http as http
import pyodbc
from data.endpoints import loginInit, loginConfirm, setPin, sendOtp, createSession, zagadki


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Headers(Singleton):

    def default_header(self, session):
        headers = {'SessionToken': session['sessiontoken'],
                   'Content-Type': r'application/json; charset=UTF-8'}
        return headers


class DbConnect(Singleton):

    def __init__(self):
        self.server = 'T-tdabb1-cdl01.abb-win.akbars.ru'
        self.database = ''
        self.username = ''
        self.password = ''

    def db_connect(self):
        try:
            cnxn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            cursor = cnxn.cursor()
            return cursor
        except:
            return False


class Session(Singleton):

    def __init__(self):
        self.session_atr = {
            'session_key': '',
            'devicetoken': '',
            'operationid': '',
            'refreshtoken': '',
            'sessiontoken': '',
            'optime': '',
            'pushtoken': '',
            'otp': '',
            'needotp': '',
            'testuser': said,
            'host': 'http://testbankok.akbars.ru',
            'operationToken': '',
            'otpCode': ''
        }

    def create_session(self):
        login_init(self.session_atr)
        login_confirm(self.session_atr)
        set_pin(self.session_atr)
        create_session(self.session_atr)
        self.session_atr['sessiontoken'] = create_session(self.session_atr)
        print("Сессия: ", self.session_atr['sessiontoken'])


def login_init(session):
    resp = http.parametrized_post(host=session['host'],
                                  endpoint=loginInit,
                                  body_payload={'login': session['testuser']['login'],
                                                'password': session['testuser']['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    session['needotp'] = resp['Result']['NeedOtp']
    if session['needotp'] is True:
        send_otp(session)
        get_otp(session)
    return resp


def login_confirm(session):
    resp = http.parametrized_post(host=session['host'],
                                  endpoint=loginConfirm,
                                  body_payload={'AkbarsOnlineLoginOperationId': session['operationid'],
                                                'DeviceToken': session['devicetoken'], 'otpCode': session['otp']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return resp


def set_pin(session):
    resp = http.parametrized_post(host=session['host'],
                                  endpoint=setPin,
                                  body_payload={'RefreshToken': session['refreshtoken'],
                                                'Pin': session['testuser']['pin'],
                                                'DeviceToken': session['devicetoken']})
    return resp


def create_session(session):
    resp = http.parametrized_post(host=session['host'],
                                  endpoint=createSession,
                                  body_payload={'RefreshToken': session['refreshtoken'],
                                                'Pin': session['testuser']['pin']})

    session_token = resp['Result']['SessionToken']
    return session_token


def send_otp(session):
    resp = http.parametrized_post(host=session['host'],
                                  endpoint=sendOtp,
                                  body_payload={'AkbarsOnlineLoginOperationId': session['operationid']},
                                  header_payload={'Content-Type': r'application/json; charset=UTF-8'})
    return resp


def get_otp(session):
    resp = http.parametrized_get(host=session['host'],
                                 endpoint=zagadki,
                                 url_payload={"operationToken": "IdentityAbo:" + session['operationid']})
    session['otp'] = resp['code']
    return resp

# s = Session()
# print("Object created", s)
# s1 = Session()
# print("Object created", s1)
