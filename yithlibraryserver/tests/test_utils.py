# Yith Library Server is a password storage server.
# Copyright (C) 2013 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# This file is part of Yith Library Server.
#
# Yith Library Server is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Yith Library Server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Yith Library Server.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from yithlibraryserver.utils import remove_attrs

class UtilsTests(unittest.TestCase):

    def test_remove_attrs(self):
        self.assertEqual({}, remove_attrs({}))
        self.assertEqual({'a': 1, 'b': 2}, remove_attrs({'a': 1, 'b': 2}))
        self.assertEqual({'a': 1, 'b': 2}, remove_attrs({'a': 1, 'b': 2}, 'c', 'd'))
        self.assertEqual({'a': 1, 'b': 2}, remove_attrs({'a': 1, 'b': 2, 'c': 3}, 'c', 'd'))
