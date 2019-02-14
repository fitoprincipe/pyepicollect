# -*- coding: utf-8 -*-

""" Batch processes for Epi Collect """
from . import api
import os


def download_media(slug, name, file_type, file_format=None, path=None,
                   token=None, stream=True):
    """ Download Media data

    :param name: the name for the file
    :type name: str
    :param file_type: The type of media. One of 'photo', 'audio', 'video'
    :type file_type: str
    :param file_format: The file_format of the media. Depends on the type.
    See url
    :type file_format: str
    :param path: the path to download the file
    :type path: str
    :param stream: stream the data to download
    :type stream: bool
    """
    response = api.get_media(
        slug=slug,
        name=name,
        file_type=file_type,
        file_format=file_format,
        token=token,
        stream=stream)

    if not path:
        path = os.getcwd()

    name = os.path.join(path, name)

    with open(name, "wb") as handle:
        for data in response.iter_content():
            handle.write(data)

    return handle