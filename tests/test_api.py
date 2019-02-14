# -*- coding: utf-8 -*-

""" Test api module """
import pytest
import pyepicollect as pyep

TEST_CLIENT_ID = 715
TEST_CLIENT_SECRET = '7qmNC9xmvQiLxfzN6xW0B3KfvrVyBt5JWVO8chFi'
TEST_NAME = 'Proyecto_API_Python'
TEST_SLUG = 'proyecto-api-python'


def test_search_project():
    result = pyep.api.search_project(TEST_NAME)
    ref = result['data'][0]['project']['ref']

    assert ref == 'd5b2da82934f4761aec0d4ba3de61313'


def test_get_project():
    token = pyep.auth.request_token(
        TEST_CLIENT_ID, TEST_CLIENT_SECRET)
    token = token['access_token']
    result = pyep.api.get_project(TEST_SLUG, token)

    ref = result['data']['project']['ref']

    assert ref == 'd5b2da82934f4761aec0d4ba3de61313'


def test_get_entries():
    token = pyep.auth.request_token(
        TEST_CLIENT_ID, TEST_CLIENT_SECRET)
    token = token['access_token']
    result = pyep.api.get_entries(TEST_SLUG, token)

    expected = ['meta', 'links', 'data']
    keys = list(result.keys())

    assert keys[0] in expected and keys[1] in expected and keys[2] in expected


def test_get_media():
    token = pyep.auth.request_token(
        TEST_CLIENT_ID, TEST_CLIENT_SECRET)
    token = token['access_token']
    result = pyep.api.get_media(TEST_SLUG, 'logo.jpg', 'photo',
                                file_format='project_mobile_logo', token=token)

    headers = result.headers

    assert headers['Content-Type'] == 'image/jpeg'


def test_get_media_simple():
    token = pyep.auth.request_token(
        TEST_CLIENT_ID, TEST_CLIENT_SECRET)
    token = token['access_token']
    file_name = '3fefdeb2-1080-4bbc-88f4-57b8653b0082_1549981593.jpg'
    result = pyep.api.get_media(TEST_SLUG, file_name, token=token)

    headers = result.headers

    assert headers['Content-Type'] == 'image/jpeg'
