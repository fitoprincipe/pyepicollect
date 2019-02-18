# -*- coding: utf-8 -*-
""" Authentication module for EpiCollect 5 """
import requests
from datetime import datetime

TOKEN_REQ_URL = 'https://five.epicollect.net/api/oauth/token'
REQ_URL = 'https://five.epicollect.net/api'


def request_token(client_id, client_secret):
    """ Get token. Each token is valid for 2 hours

    :return: A dictionary with the following keys:
    :rtype: dict
    """
    request = requests.post(TOKEN_REQ_URL, data={
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    })
    token_data = request.json()

    return token_data


class Auth(object):
    def __init__(self, client_id, client_secret):
        """ Auth object to hold authentication info and validate token """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.request_time = None
        self._initialized = False

    def update(self):
        """ Request token and update object """
        token = request_token(self.client_id, self.client_secret)
        self.request_time = datetime.now()
        self._initialized = True
        self.token = token

    @property
    def expires_in(self):
        """ Get seconds for the token to expire """
        if not self._initialized:
            return None

        now = datetime.now()
        delta = now - self.request_time
        ellapsed = delta.total_seconds()

        expires = self.token['expires_in'] - ellapsed

        return expires if expires > 0 else 0

    def has_expired(self):
        """ Check if token has expired based on the requested time """
        if not self._initialized:
            return True

        expires_in = self.expires_in
        if expires_in > 0:
            return False
        else:
            return True

    @property
    def access_token(self):
        """ This property will always return the access token """
        if self.has_expired():
            self.update()

        return self.token['access_token']
