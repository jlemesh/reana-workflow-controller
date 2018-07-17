# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

"""REANA Workflow Controller flask configuration."""

import os

BROKER_URL = os.getenv('RABBIT_MQ_URL',
                       'message-broker.default.svc.cluster.local')

BROKER_USER = os.getenv('RABBIT_MQ_USER', 'test')

BROKER_PASS = os.getenv('RABBIT_MQ_PASS', '1234')

BROKER = os.getenv('RABBIT_MQ', 'amqp://{0}:{1}@{2}//'.format(BROKER_USER,
                                                              BROKER_PASS,
                                                              BROKER_URL))

BROKER_PORT = os.getenv('RABBIT_MQ_PORT', 5672)

SHARED_VOLUME_PATH = os.getenv('SHARED_VOLUME_PATH', '/reana')


SQLALCHEMY_TRACK_MODIFICATIONS = False
"""Track modifications flag."""

DEFAULT_NAME_FOR_WORKFLOWS = 'workflow'
"""The default prefix used to name workflow(s): e.g. reana-1, reana-2, etc.
   If workflow is manually named by the user that prefix will used instead.
"""

WORKFLOW_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
"""Time format for workflow starting time, created time etc."""

EXCHANGE = ''

EXCHANGE_TYPE = ''

STATUS_QUEUE = 'jobs-status'

ROUTING_KEY = 'jobs-status'

POSSIBLE_JOB_STATUSES = ['submitted', 'succeeded', 'failed', 'planned']

WORKFLOW_QUEUES = {'cwl': 'cwl-default-queue',
                   'yadage': 'yadage-default-queue',
                   'serial': 'serial-default-queue'}
