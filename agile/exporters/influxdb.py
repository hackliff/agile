# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import datetime as dt

from influxdb import InfluxDBClient


def influxdb_conn(conf):
    params = {
        'host': conf.get('INFLUXDB_HOST', 'localhost'),
        'port': conf.get('INFLUXDB_PORT', 8086),
        'username': conf.get('INFLUXDB_USER', 'root'),
        'password': conf.get('INFLUXDB_PASS', 'root'),
        'database': conf.get('INFLUXDB_DB', 'test')
    }
    return InfluxDBClient(**params)


# NOTE 'fields' could be directly stats
def influxdb_export(db, repos, gh_stats, jira_stats):
    now = dt.datetime.utcnow().isoformat() + 'Z'
    json_stats = [
        {
            'measurement': 'code',
            'tags': {
                'project': repo['project'],
                'user': repo['user']
            },
            'time': now,
            'fields': {
                'open_issues': float(gh_stats[repo['project']]['issues_count']),
                'pull_requests': float(gh_stats[repo['project']]['pr_count'])
            }
        }
    for repo in repos] + [
        {
            'measurement': 'jira',
            'tags': {
                'team': 'SEED',
                'sprint': 'Sprint 11'
            },
            'time': now,
            'fields': {
                'issues': float(jira_stats['sprint_issues'])
            }
        }
    ]
    db.write_points(json_stats)
