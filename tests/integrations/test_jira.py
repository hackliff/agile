# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=pointless-statement
# pylint: disable=expression-not-assigned
# pylint: disable=missing-docstring
# pylint: disable=redefined-outer-name

import os
import pytest

# Magic injection of sure methods.
import sure
from jira import JIRA

import agile.tracker


@pytest.fixture
def jira_queries():
    return {
        'cra_issues': 'project=CRA',
        'cra_bugs': 'project=CRA and type=bugs and status="TO DO"'
    }


@pytest.fixture
def jira_credentials():
    return {
        'JIRA_USER': os.environ.get('JIRA_USER'),
        'JIRA_PASS': os.environ.get('JIRA_PASS'),
        'JIRA_SERVER': os.environ.get('JIRA_SERVER')
    }


@pytest.fixture
def official_jira_conn():
    return JIRA(agile.tracker.OFFICIAL_JIRA_SERVER)


def test_jira_credentials(jira_credentials):
    (jira_credentials.get('JIRA_USER')).should_not.be.none
    (jira_credentials.get('JIRA_PASS')).should_not.be.none
    (jira_credentials.get('JIRA_SERVER')).should_not.be.none


def test_jira_connection(jira_credentials):
    conn = agile.tracker.login(jira_credentials)
    (conn).should_not.be.none


def test_jira_official_conn(official_jira_conn):
    (official_jira_conn).should_not.be.none


# def test_jira_stats(official_jira_conn, jira_queries):
    # stats = agile.tracker.search_stats(official_jira_conn, jira_queries)
