# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import github3


def github_conn(conf):
    user = conf.get('GITHUB_USER')
    pwd = conf.get('GITHUB_PASS')
    return github3.login(user, pwd)


def github_stats(gh, user, repo):
    repo = gh.repository(user, repo)
    pull_requests = [pr for pr in repo.iter_pulls(state='open')]
    return {
        'issues_count': repo.open_issues,
        'pr_count': len(pull_requests)
    }
