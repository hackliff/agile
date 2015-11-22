# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import datetime as dt

import yaml


def load_config(conf_fd):
    """Load what to measure on Github and Jira.

    :param conf_path: yaml configuration file (file descriptor)
    """
    return yaml.load(conf_fd)


def utcnow():
    """ISO 8601 format for UTC now."""
    return dt.datetime.utcnow().isoformat() + 'Z'


def cascade(conf, keys, default):
    """Try several keys to extract data from a dict."""
    for k in keys:
        value = conf.get(k)
        if value is not None:
            return value
    return default
