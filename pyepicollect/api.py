# -*- coding: utf-8 -*-

""" Main API calls """
from . import auth
import requests
import os

MEDIA_TYPES = ['photo', 'audio', 'video']


def search_project(name):
    """ Search a Project based on it's name """
    url = '{}/projects/{}'.format(auth.REQ_URL, name)
    response = requests.get(url)

    return response.json()


def get_project(slug, token=None):
    """ Get a Project based on it's slug

    https://epicollect5.gitbooks.io/epicollect5-api/project/export-project.html
    """
    url = '{}/export/project/{}'.format(auth.REQ_URL, slug)

    if not token:
        response = requests.get(url)
    else:
        response = requests.get(
            url,
            headers={'Authorization': 'Bearer ' + token}
        )

    return response.json()


def get_entries(slug, token=None, **kwargs):
    """ Get Entries. Extra params can be found on the web:

    https://epicollect5.gitbooks.io/epicollect5-api/entries.html
    """
    url = '{}/export/entries/{}'.format(auth.REQ_URL, slug)

    if not token:
        response = requests.get(url, params=kwargs)
    else:
        response = requests.get(
            url,
            headers={'Authorization': 'Bearer ' + token},
            params=kwargs
        )

    return response.json()


def get_media(slug, name, type, format=None, token=None, stream=True):
    """ Get Media data

    https://epicollect5.gitbooks.io/epicollect5-api/media/get-media.html

    :param name: the name of the file to download
    :type name: str
    :param type: The type of media. One of 'photo', 'audio', 'video'
    :type type: str
    :param format: The format of the media. Depends on the type. See url
    :type format: str
    """
    url = '{}/export/media/{}'.format(auth.REQ_URL, slug)

    if type not in MEDIA_TYPES:
        raise ValueError(
            'type parameter must be one of {}'.format(MEDIA_TYPES))

    if not format:
        formats = {'photo': 'entry_original',
                   'audio': 'audio',
                   'video': 'video'}
        format = formats[type]

    params = {'type': type, 'format': format, 'name': name}

    if not token:
        response = requests.get(url, params=params, stream=stream)
    else:
        response = requests.get(
            url,
            headers={'Authorization': 'Bearer ' + token},
            params= params,
            stream= stream
        )

    return response


def download_media(slug, name, type, format=None, path=None, token=None,
                   stream=True):
    """ Download Media data

    https://epicollect5.gitbooks.io/epicollect5-api/media/get-media.html

    :param name: the name for the file
    :type name: str
    :param type: The type of media. One of 'photo', 'audio', 'video'
    :type type: str
    :param format: The format of the media. Depends on the type. See url
    :type format: str
    :param path: the path to download the file
    :type path: str
    :param stream: stream the data to download
    :type stream: bool
    """
    response = get_media(
        slug=slug,
        name=name,
        type=type,
        format=format,
        token=token,
        stream=stream)

    if not path:
        path = os.getcwd()

    name = os.path.join(path, name)

    with open(name, "wb") as handle:
        for data in response.iter_content():
            handle.write(data)

    return handle
