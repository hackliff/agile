# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=pointless-statement

# Magic injection of sure methods.
import sure

import agile.utils

FIXTURE_CONF_FILE = './tests/fixtures/conf.yml'
EXPECTED_QUERIES = {
    'sprint_tickets': 'project=SEED and sprint=\'Sprint 11\''
}


def test_random_color_in_click_list():
    conf = agile.utils.load_config(FIXTURE_CONF_FILE)
    (conf['repos']).should.have.length_of(3)
    (conf).should.have.key('queries').being.equal(EXPECTED_QUERIES)
