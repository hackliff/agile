# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import yaml

def load_config(conf_path):
    """Load what to measure on Github and Jira.

    :param conf_path: yaml configuration file (str)
    """
    with open(conf_path, 'r') as conf_fd:
        return yaml.load(conf_fd)
