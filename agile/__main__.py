#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# pylint: disable=no-value-for-parameter

"""Agile development workflow, measured.
"""

import click

import agile.utils

# repos = [
    # {'user': 'Appturbo', 'project': 'octopus'},
    # {'user': 'Appturbo', 'project': 'iron-legion'},
    # {'user': 'Appturbo', 'project': 'hawkeye'}
# ]

# seeding_project_id = 10500
# seeding_board_id = 8
# seeding_sprint_11_id = 83
# queries = {
    # 'sprint_issues': 'project=SEED and sprint="Sprint 11"'
# }


@click.command()
@click.option('--config', default='./agile.yml', help='Configuration file path.')
def run(config):
    """Gather tools metrics and export them."""
    params = agile.utils.load_config(config)
    print(params)
    # db = influxdb_conn(os.environ)
    # gh = github_conn(os.environ)
    # gh_stats = {}
    # for repo in repos:
        # gh_stats[repo['project']] = github_stats(gh, repo['user'], repo['project'])
    # jira = jira_conn(os.environ)
    # jira_stats = search_jira_stats(jira)

    # influxdb_export(gh_stats, jira_stats)


if __name__ == '__main__':
    run()

