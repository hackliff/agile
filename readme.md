# Agile Workflow Analytics

[![Circle CI](https://circleci.com/gh/hackliff/agile.svg?style=svg)](https://circleci.com/gh/hackliff/agile)
[![codecov.io](https://codecov.io/github/hackliff/agile/coverage.svg?branch=master)](https://codecov.io/github/hackliff/agile?branch=master)


- [Github3 doc][gh3]
- [Jira python doc][jyra]
- [InfluxDB Python SDK][ynflux]

- [Ring 3 inspiration][inspiration]

## Usage

```Bash
influx -execute 'CREATE DATABASE agile'

agile --config=./conf.yml --export=db
```

---

## [Jira Query Language][jql]

Interesting queries:
    project=SEED
    sprint='Sprint 11'
    status=resolved/Open
    type=Bug
    status WAS "Resolved/In Progress" BY jsmith
    priority in (Blocker, Critical)
    priority=urgent/High
    assignee/reporter=EMPTY
    created < -1d
    duedate < now()
    "epic link" = Jupiter
    originalEstimate > 2d
    remainingEstimate > 4h
    timeSpent > 5d
    workRatio > 75

Interesting questions:
  how many issues opened in progress/todo/done
  how many hours/days left for this sprint
  how much time logged by the team each day
  how many bugs



[gh3]: http://github3py.readthedocs.org/en/master/
[jyra]: http://jira.readthedocs.org/en/latest/
[ynflux]: http://influxdb-python.readthedocs.org/en/latest
[inspiration]: https://github.com/simonjbeaumont/ring3-dash
[jql]: https://confluence.atlassian.com/jira/advanced-searching-179442050.html
