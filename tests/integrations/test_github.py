# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=pointless-statement
# pylint: disable=expression-not-assigned
# pylint: disable=missing-docstring
# pylint: disable=redefined-outer-name

import os
import random
import pytest

# Magic injection of sure methods.
import sure

import agile.code


@pytest.fixture
def gh_credentials():
    return {
        'GITHUB_USER': os.environ.get('GITHUB_USER'),
        'GITHUB_PASS': os.environ.get('GITHUB_PASS')
    }


@pytest.fixture
def repo():
    return random.choice([
        {'user': 'plotly', 'project': 'plotly.js'}
    ])


def test_github_credentials(gh_credentials):
    (gh_credentials.get('GITHUB_USER')).should_not.be.none
    (gh_credentials.get('GITHUB_PASS')).should_not.be.none


def test_github_loginion(gh_credentials):
    conn = agile.code.login(gh_credentials)
    (conn).should_not.be.none


def test_github_stats_format(gh_credentials, repo):
    conn = agile.code.login(gh_credentials)
    stats = agile.code.stats(conn, repo['user'], repo['project'])
    stats.should.have.key('measurement').being.equal('code')
    stats.should.have.key('tags').being.a('dict')
    stats.should.have.key('time')
    stats.should.have.key('fields').being.a('dict')


def test_github_stats_issues(gh_credentials, repo):
    conn = agile.code.login(gh_credentials)
    stats = agile.code.stats(conn, repo['user'], repo['project'])
    stats['fields'].should.have.key('issues_count').being.greater_than_or_equal_to(0.0)


def test_github_stats_pull_requests(gh_credentials, repo):
    conn = agile.code.login(gh_credentials)
    stats = agile.code.stats(conn, repo['user'], repo['project'])
    stats['fields'].should.have.key('pr_count').being.greater_than_or_equal_to(0.0)
