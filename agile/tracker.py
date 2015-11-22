# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os

from jira import JIRA

import agile.utils

OFFICIAL_JIRA_SERVER = 'https://jira.atlassian.com'


def login(conf=None):
    """Login on Jira server.

    args:
        conf (dict) -- credentials container (default: os.environ). It is expected
                       to store JIRA_USER, JIRA_PASS and optionaly JIRA_SERVER values.

    raises:
        jira.JIRAError -- on bad credentials

    returns:
        jira.client.JIRA -- authentified connection to Jira
    """
    conf = conf or os.environ
    user = conf.get('JIRA_USER')
    pwd = conf.get('JIRA_PASS')
    options = {
        'server': conf.get('JIRA_SERVER', OFFICIAL_JIRA_SERVER)
    }
    return JIRA(options, basic_auth=(user, pwd))


def search_stats(conn, queries):
    """Search for jira project information, using jql

    see https://confluence.atlassian.com/jira/advanced-searching-179442050.html
    for details on the JQL syntax.

    args:
        conn (jira.client.JIRA) -- authentified connection to jira
        queries (dict) -- jql statements associated with a title

    raises:
        jira.JIRAError -- on unexpected server responses

    returns:
        dict -- queries result assciated with the title
    """
    stats = {}
    for title, jql in queries.items():
        res = conn.search_issues(jql, maxResults=1, fields='key', json_result=True)
        stats[title] = float(res['total'])
    return {
        'measurement': 'jira',
        'tags': {
            'team': 'SEED',
            'sprint': 'Sprint 11'
        },
        'time': agile.utils.utcnow(),
        'fields': stats
    }
