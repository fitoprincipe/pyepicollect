# -*- coding: utf-8 -*-

""" Test auth module """
import pytest
import pyepicollect


def test_request_token():
    client_id = 715
    client_secret = '7qmNC9xmvQiLxfzN6xW0B3KfvrVyBt5JWVO8chFi'

    token = pyepicollect.auth.request_token(client_id, client_secret)

    assert type(token) is dict