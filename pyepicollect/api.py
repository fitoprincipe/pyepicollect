# -*- coding: utf-8 -*-

""" Main API calls """
from . import auth
import requests

MEDIA_TYPES = ['photo', 'audio', 'video']
EXT_PHOTO = ['gif', 'ico', 'jpeg', 'jpg', 'svg', 'tiff', 'tif', 'webp']
EXT_AUDIO = ['aac', 'mid', 'midi', 'ogg', 'wav', 'weba', '3gp', '3g2']
EXT_VIDEO = ['avi', 'mpeg', 'mpg', 'ogv', 'webm', '3gp', '3g2']


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


def get_branch_entries(slug, branch, token=None, **kwargs):
    """ Get the branch entries for a particular Branch in a Form for a Project

    https://epicollect5.gitbooks.io/epicollect5-api/get-branch-entries.html

    :param slug: The slugified project name
    :param branch: The ref of a branch input in a form
    :param token: access token
    :param kwargs: extra arguments. See URL
    """
    return get_entries(slug, token, branch_ref=branch, **kwargs)


def get_media(slug, name, file_type=None, file_format=None, token=None,
              stream=True):
    """ Get Media data

    https://epicollect5.gitbooks.io/epicollect5-api/media/get-media.html

    To get the binary content of the fetched data do:

    ```python
    media = api.get_media(**kwargs)
    binary_data = media.content
    ```

    :param name: the name of the file to download
    :type name: str
    :param file_type: The type of media. One of 'photo', 'audio', 'video'
    :type file_type: str
    :param file_format: The format of the media. Depends on the type. See url
    :type file_format: str
    :return: a response object (see http://docs.python-requests.org/en/latest/user/quickstart/#response-content)
    :rtype: requests.models.Response
    """
    url = '{}/export/media/{}'.format(auth.REQ_URL, slug)

    if file_type and file_type not in MEDIA_TYPES:
        raise ValueError(
            'file_type parameter must be one of {}'.format(MEDIA_TYPES))

    if not file_type:
        # get file extension
        try:
            ext = name.split('.')[1]
        except IndexError:
            raise ExtensionError
        else:
            if ext in EXT_PHOTO:
                file_type = 'photo'
            elif ext in EXT_AUDIO:
                file_type = 'audio'
            elif ext in EXT_VIDEO:
                file_type = 'video'
            else:
                raise ExtensionError

    if not file_format:
        formats = {'photo': 'entry_original',
                   'audio': 'audio',
                   'video': 'video'}
        file_format = formats[file_type]

    params = {'type': file_type, 'format': file_format, 'name': name}

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


# Custom Exceptions
class ExtensionError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = 'The name does not contain an extension, please provide'\
                      ' a file_type with parameter file_type'
        super(ExtensionError, self).__init__(message)
