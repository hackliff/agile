# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Print and style information on stdout.
"""

import click

OUTPUT_COLOR = 'blue'


def prefix(name):
    return click.style('{:<10} | '.format(name), fg=OUTPUT_COLOR)

def export(stats):
    for data in stats:
        content = ' '.join(['{}={}'.format(k, v) for k, v in data['fields'].items()])
        content = click.style(content, bold=True, fg=OUTPUT_COLOR)
        click.echo('{}{}'.format(prefix(data['measurement']), content))
