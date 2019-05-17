# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *

from targets.firefox.firefox_ui.private_window import PrivateWindow


class Test(FirefoxTest):

    @pytest.mark.details(
        description='Private Browsing window is not restored after Firefox crash',
        test_case_id='101748',
        test_suite_id='1826',
        locale=['en-US'],
        enabled=False
    )
    def run(self, firefox):
        restart_firefox_button_pattern = Pattern('restart_firefox_button.png')
        soap_wikipedia_header_label_pattern = Pattern('soap_wikipedia_header_label.png')

        firefox.restart()

        new_private_window()

        private_browsing_window_opened = exists(PrivateWindow.private_window_pattern, 5)
        assert private_browsing_window_opened is True, 'Private Browsing Window opened'

        navigate(LocalWeb.SOAP_WIKI_TEST_SITE)
        soap_label_exists = exists(LocalWeb.SOAP_WIKI_SOAP_LABEL, 20)
        assert soap_label_exists is True, 'The page is successfully loaded.'

        navigate('about:crashparent')

        firefox.restart()

        if Settings.is_windows():
            crash_reporter_icon_pattern = Pattern('crash_reporter_icon.png')
            crash_reporter_icon_exists = exists(crash_reporter_icon_pattern, 180)
            assert crash_reporter_icon_exists is True, 'Crash Reporter icon exists'
            click(crash_reporter_icon_pattern)

        firefox_crashed = exists(restart_firefox_button_pattern, 10)
        assert firefox_crashed is True, 'Firefox crashed.'

        click(restart_firefox_button_pattern)

        try:
            crash_report_dismissed = wait_vanish(restart_firefox_button_pattern, 180)
            assert crash_report_dismissed is True, 'Crash report dismissed'
        except FindError:
            raise FindError('Crash report is not dismissed')

        restore_session_exists = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert restore_session_exists is True, 'Firefox restored'

        wiki_label_exists = exists(soap_wikipedia_header_label_pattern, 2)
        assert wiki_label_exists is False, 'The Private Browsing window is not restored.'
