# -*- coding: utf-8 -*-
# Copyright 2007-2017 UShareSoft SAS, All rights reserved
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest

import pyxb
from mock import patch
from uforge.application import Api
from uforge.objects import uforge

from hammr.commands.migration import migration
from hammr.utils import constants


class MyTestCase(unittest.TestCase):
    @patch('uforge.application.Api._Users._Migrations.Getall')
    @patch('texttable.Texttable.add_row')
    def test_do_list_list_all_the_migrations(self, mock_table_add_row, mock_api_getall):
        # given
        m = migration.Migration()
        m.api = Api("url", username="username", password="password", headers=None,
                    disable_ssl_certificate_validation=False, timeout=constants.HTTP_TIMEOUT)
        m.login = "login"
        m.password = "password"
        self.create_migration(mock_api_getall, 1, "a migration", 50, False)

        # when
        m.do_list("")

        # then
        self.assertEquals(mock_table_add_row.call_count, 1)
        mock_table_add_row.assert_called_with([1, "a migration", "status (50%)"])

    @patch("ussclicore.utils.printer.out")
    @patch('uforge.application.Api._Users._Migrations.Getall')
    def test_do_list_return_no_migration_message_when_there_is_no_migration(self, mock_api_getall, mock_message):
        # given
        m = migration.Migration()
        m.api = Api("url", username="username", password="password", headers=None,
                    disable_ssl_certificate_validation=False, timeout=constants.HTTP_TIMEOUT)
        m.login = "login"
        m.password = "password"
        self.create_migration(mock_api_getall, 0, "", 0, True)

        # when
        m.do_list("")

        # then
        mock_message.assert_called_with("No migrations available")

    def create_migration(self, mock_api_getall, id, name, percentage, empty):
        migrations = uforge.migrations()
        migrations.migrations = pyxb.BIND()

        if not empty:
            migration = uforge.migration()
            migration.dbId = id
            migration.name = name

            status = uforge.status()
            status.message = "status"
            status.percentage = percentage
            status.complete = False

            migration.status = status
            migrations.migrations.append(migration)

        mock_api_getall.return_value = migrations
