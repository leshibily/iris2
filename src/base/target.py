# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

class BaseTarget(object):

    def __init__(self):
        self.target_name = 'Default target'
        self.cc_settings = {}