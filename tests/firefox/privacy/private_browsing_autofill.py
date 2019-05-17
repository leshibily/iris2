# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *


class Test(FirefoxTest):

    @pytest.mark.details(
        description='The form inputs that were previously saved in a normal session are remembered in Private '
                    'Browsing session.',
        locale=['en-US'],
        test_case_id='101666',
        test_suite_id='1826',
        set_profile_pref = {'extensions.formautofill.available': 'on'},
        blocked_by = 'set_profile_pref, change_preference() don\'t work properly'
    )
    def run(self, firefox):
        name_field_pattern = Pattern('name_field.png').similar(.6)
        private_browsing_image_pattern = PrivateWindow.private_window_pattern
        saved_profiles_pattern = Pattern('saved_profiles.png').similar(.6)
        if OSHelper.is_mac():
            additional_saved_profiles_pattern = Pattern('additional_saved_profiles.png').similar(.6)

        find_in_preferences_field_pattern = AboutPreferences.PRIVACY_AND_SECURITY_BUTTON_SELECTED
        saved_addresses_button_pattern = Pattern('saved_addresses_button.png')
        add_button_pattern = Pattern('add_button.png')

        change_preference('browser.search.region', 'US')

        firefox.restart()

        navigate('about:preferences#privacy')

        search_field_exists = exists(find_in_preferences_field_pattern, Settings.FIREFOX_TIMEOUT)
        assert search_field_exists, 'Preferences page is opened'

        type('Autofill')

        saved_addresses_button_exists = exists(saved_addresses_button_pattern)
        assert saved_addresses_button_exists, '\'Saved addresses\' button is displayed on the Preferences page'

        click(saved_addresses_button_pattern)

        add_button_exists = exists(add_button_pattern)
        assert add_button_exists, '\'Add\' button is displayed on the \'Saved addresses\' popup'

        click(add_button_pattern)

        navigate('https://luke-chang.github.io/autofill-demo/basic.html')

        input_data = ['Maria V. Griggs', 'Loblaws', '1223 Rainbow Drive', 'Youngstown, OH', '1223 Rainbow Drive',
                      '44512', 'US', '9079782387', 'maria_griggs@gmail.com']
        input_data_2 = ['Second V. Griggs', 'Loblaws_2', '1223 Rainbow Drive_2', 'Youngstown, OH_2',
                        '1223 Rainbow Drive_2', '44512', 'US', '9079782387', 'second_griggs@gmail.com']

        name_field_exists = exists(name_field_pattern, Settings.SITE_LOAD_TIMEOUT)
        assert name_field_exists, 'The basic forms Autofill demo is opened'

        click(name_field_pattern)

        for fields in range(9):
            type(input_data[fields])
            type('\t')

        type('\n')

        restore_firefox_focus()

        click(name_field_pattern)

        for fields in range(9):
            type(input_data_2[fields])
            type('\t')

        type('\n')

        click(name_field_pattern)

        double_click(name_field_pattern)

        if Settings.is_mac():
            saved_profiles_exists = exists(saved_profiles_pattern, Settings.FIREFOX_TIMEOUT)
            additional_saved_profiles_exists = exists(additional_saved_profiles_pattern, Settings.FIREFOX_TIMEOUT)
            assert saved_profiles_exists or additional_saved_profiles_exists, 'The Name from the saved profile is ' \
                                                                              'displayed in the drop down'
        else:
            saved_profiles_exists = exists(saved_profiles_pattern, Settings.FIREFOX_TIMEOUT)
            assert saved_profiles_exists, 'The Name from the saved profile is displayed in the drop down'

        new_private_window()

        private_browsing_opened = exists(private_browsing_image_pattern, Settings.FIREFOX_TIMEOUT)
        assert private_browsing_opened, 'Private browsing window is opened'

        navigate('https://luke-chang.github.io/autofill-demo/basic.html')

        name_field_exists_private = exists(name_field_pattern, Settings.SITE_LOAD_TIMEOUT)
        assert name_field_exists_private, 'The basic forms Autofill demo is opened'

        click(name_field_pattern)

        double_click(name_field_pattern)

        if Settings.is_mac():
            saved_profiles_exists_private = exists(saved_profiles_pattern, Settings.FIREFOX_TIMEOUT)
            additional_saved_profiles_exists_private = exists(additional_saved_profiles_pattern,
                                                              Settings.FIREFOX_TIMEOUT)
            assert saved_profiles_exists_private or additional_saved_profiles_exists_private, 'The Name from the ' \
                'saved profile is displayed in the drop down in Private browsing'
        else:
            saved_profiles_exists_private = exists(saved_profiles_pattern, Settings.FIREFOX_TIMEOUT)
            assert saved_profiles_exists_private, 'The Name from the saved profile is displayed in the drop down ' \
                                                  'in Private browsing'

        close_window()
