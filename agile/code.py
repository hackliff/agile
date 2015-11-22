# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os

import github3

import agile.utils


def login(conf=None):
    """Log in on the given github account

    args:
        conf (dict) -- user credentials, with expected keys GITHUB_USER and
                       GITHUB_PASS
    returns:
        github3.github.Github or None -- authenticated github connection
    """
    conf = conf or os.environ
    user = conf.get('GITHUB_USER')
    pwd = conf.get('GITHUB_PASS')
    return github3.login(user, pwd)


def stats(gh, user, project):
    repo = gh.repository(user, project)
    pull_requests = [pr for pr in repo.iter_pulls(state='open')]
    return {
        'measurement': 'code',
        'tags': {
            'project': project,
            'user': user
        },
        'time': agile.utils.utcnow(),
        'fields': {
            'issues_count': float(repo.open_issues),
            'pr_count': float(len(pull_requests))
        }
    }
