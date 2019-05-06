# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from targets.firefox.fx_testcase import *


class Test(FirefoxTest):

    @pytest.mark.details(
            description='This test case checks that navigation to a page without entering the \'http://\' protocol '
                        'works correctly.',
            locale=[Locales.ENGLISH, Locales.CHINESE, Locales.SPANISH, Locales.FRENCH, Locales.GERMAN, Locales.ARABIC,
                    Locales.RUSSIAN, Locales.KOREAN, Locales.PORTUGUESE, Locales.VIETNAMESE, Locales.POLISH,
                    Locales.TURKISH, Locales.ROMANIAN, Locales.JAPANESE],
            test_case_id='117529',
            test_suite_id='1902'
    )
    def run(self, firefox):

        apache_logo_pattern = Pattern('apache_logo.png')

        navigate('httpd.apache.org')

        expected = exists(apache_logo_pattern, 10)
        assert expected, 'Page successfully loaded, Apache logo found.'
