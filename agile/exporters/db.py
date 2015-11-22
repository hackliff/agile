# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os

from influxdb import InfluxDBClient

import agile.utils

DEFAULT_INFLUX_HOST = 'localhost'
DEFAULT_INFLUX_PORT = 8086


def connect(conf=None):
    conf = conf or os.environ
    host_keys = ['INFLUX_HOST', 'INFLUXDB_PORT_8086_TCP_ADDR']
    port_keys = ['INFLUX_PORT', 'INFLUXDB_PORT_8086_TCP_PORT']
    params = {
        'host': agile.utils.cascade(conf, host_keys, DEFAULT_INFLUX_HOST),
        'port': agile.utils.cascade(conf, port_keys, DEFAULT_INFLUX_PORT),
        'username': conf.get('INFLUX_USER', 'root'),
        'password': conf.get('INFLUX_PASS', 'root'),
        'database': conf.get('INFLUX_DB', 'agile')
    }
    print('connecting to influxdb {}'.format(params))
    return InfluxDBClient(**params)


def export(db, stats):
    print('saving statistics: {}'.format(stats))
    db.write_points(stats)
