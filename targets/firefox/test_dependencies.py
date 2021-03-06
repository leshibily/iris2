# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.firefox_app.fx_browser import Profiles, FirefoxUtils
from targets.firefox.firefox_ui.bookmarks import Bookmarks
from targets.firefox.firefox_ui.helpers.history_test_utils import open_clear_recent_history_window
from targets.firefox.firefox_ui.helpers.keyboard_shortcuts import *
from targets.firefox.firefox_ui.helpers.update_rules import is_update_required, get_rule_for_channel, get_update_rules
from targets.firefox.firefox_ui.history import History
from targets.firefox.firefox_ui.library import Library
from targets.firefox.firefox_ui.library_menu import LibraryMenu
from targets.firefox.firefox_ui.sidebar import Sidebar
from targets.firefox.firefox_ui.test_utils import restore_firefox_focus, open_clear_recent_history_window
from targets.firefox.local_web.web_links.local_web import LocalWeb
from targets.firefox.firefox_ui.utils import Utils
from targets.firefox.firefox_ui.helpers.general import *
from targets.firefox.firefox_ui.helpers.history_test_utils import *
from targets.firefox.firefox_ui.tabs import Tabs
from targets.firefox.firefox_ui.download_dialog import DownloadDialog
from targets.firefox.firefox_ui.about_preferences import AboutPreferences