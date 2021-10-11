from __future__ import unicode_literals
import logging

import requests
import json


def notify(title, message, retcode=None, webhook=None):
    """
    Required parameter:
        * ``webhook`` - The webhook link, created in Teams
    """

    logger = logging.getLogger(__name__)
    if webhook is None:
        logger.error('please set webhook variable under '
                     'teams backend of the config file')
        return
    headers = { 'Content-Type': 'application/json' }
    data = { "title": message, "text": title }
    response = requests.post(
        webhook,
        headers=headers,
        data=json.dumps(data))
    response.raise_for_status()
