#
# Copyright (C) 2016 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
#

from datetime import timedelta

from oslo_config import cfg
from oslo_log import log as logging

from networking_odl.common import constants as odl_const
from networking_odl.db import db

LOG = logging.getLogger(__name__)


class JournalCleanup(object):
    """Journal maintenance operation for deleting completed rows."""
    def __init__(self):
        self._rows_retention = cfg.CONF.ml2_odl.completed_rows_retention

    def delete_completed_rows(self, session):
        if self._rows_retention is not -1:
            LOG.debug("Deleting completed rows")
            db.delete_rows_by_state_and_time(
                session, odl_const.COMPLETED,
                timedelta(seconds=self._rows_retention))
