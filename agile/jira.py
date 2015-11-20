# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import sys

from jira import JIRA, JIRAError


def jira_conn(conf):
    user = conf.get('JIRA_USER')
    pwd = conf.get('JIRA_PASS')
    options = {
        'server': 'https://appturbo.atlassian.net'
    }
    return JIRA(options, basic_auth=(user, pwd))


def search_jira_stats(conn, queries):
    stats = {}
    for key, jql in queries.items():
        try:
            res = conn.search_issues(jql, maxResults=1, fields='key', json_result=True)
            stats[key] = res['total']
        except JIRAError as err:
            sys.stderr.write('error: Could not retrieve_counts from JIRA: {}'.format(err))
            sys.exit(1)
    return stats
