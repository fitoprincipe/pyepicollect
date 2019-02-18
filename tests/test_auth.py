# -*- coding: utf-8 -*-

""" Test auth module """
import pytest
import pyepicollect as pyep

TEST_CLIENT_ID = 715
TEST_CLIENT_SECRET = '7qmNC9xmvQiLxfzN6xW0B3KfvrVyBt5JWVO8chFi'
TEST_NAME = 'Proyecto_API_Python'
TEST_SLUG = 'proyecto-api-python'


def test_request_token():
    token = pyep.auth.request_token(
    TEST_CLIENT_ID, TEST_CLIENT_SECRET)

    assert type(token) is dict


def test_Auth_access_token():
    auth = pyep.Auth(TEST_CLIENT_ID, TEST_CLIENT_SECRET)

    access_token = auth.access_token
    assert type(access_token) is str


def test_Auth_update():
    auth = pyep.Auth(TEST_CLIENT_ID, TEST_CLIENT_SECRET)
    auth.update()
    request_time = auth.request_time

    from datetime import timedelta
    delta = timedelta(1)  # 1 day

    auth.request_time = request_time - delta

    access_token = auth.access_token
    assert type(access_token) is str