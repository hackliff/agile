#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# pylint: disable=no-value-for-parameter

"""Agile development workflow, measured.
"""

import sys

import click

import agile.utils
import agile.tracker
import agile.code
import agile.exporters.shell as shell
import agile.exporters.db as db


def inspect_github(conf):
    """Gather projects' stats on Github."""
    # expect credentials to be exported in the environment
    gh_conn = agile.code.login()
    if gh_conn is None:
        print('github log in failed')
        sys.exit(1)

    return [
        agile.code.stats(gh_conn, repo['user'], repo['project'])
        for repo in conf['repos']
    ]


@click.command()
@click.option('--config',
              default='./agile.yml',
              type=click.File('r'),
              help='Configuration file path.')
@click.option('--exporter',
              default='shell',
              help='Statistics exporter (shell, db).')
def run(config, exporter):
    """Gather tools metrics and export them."""
    try:
        params = agile.utils.load_config(config)
    except FileNotFoundError as err:
        click.echo('failed to load configuration: {}'.format(err))
        sys.exit(1)

    gh_stats = inspect_github(params)

    # expect credentials to be exported in the environment
    jira = agile.tracker.login()
    jira_stats = agile.tracker.search_stats(jira, params['queries'])

    if exporter == 'db':
        influxdb = db.connect()
        db.export(influxdb, gh_stats + [jira_stats])
    elif exporter == 'shell':
        shell.export(gh_stats + [jira_stats])
    else:
        raise ValueError('unsupported exporter: {}'.format(exporter))


if __name__ == '__main__':
    run()

