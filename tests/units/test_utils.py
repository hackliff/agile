# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=pointless-statement
# pylint: disable=missing-docstring
# pylint: disable=redefined-outer-name

# Magic injection of sure methods.
import sure
import pytest
import dateutil.parser

import agile.utils

FIXTURE_CONF_FILE = './tests/fixtures/conf.yml'
EXPECTED_QUERIES = {
    'sprint_tickets': 'project=SEED and sprint=\'Sprint 11\''
}


@pytest.fixture
def conf_fd():
    return open(FIXTURE_CONF_FILE, 'r')


def test_load_yaml_configuration(conf_fd):
    conf = agile.utils.load_config(conf_fd)
    conf.should.be.a('dict')
    (len(conf['repos'])).should.be.greater_than(0)
    (conf).should.have.key('queries')
    conf_fd.close()


def test_utcnow():
    now = agile.utils.utcnow()
    date = dateutil.parser.parse(now)
    date.tzname().should.equal('UTC')


def test_cascade_find_value():
    value = 'bar'
    res = agile.utils.cascade({'foo': value}, ['whatever', 'foo'], 'default')
    res.should.equal(value)


def test_cascade_default_value():
    default = 'bar'
    res = agile.utils.cascade({}, ['foo'], default)
    res.should.equal(default)
