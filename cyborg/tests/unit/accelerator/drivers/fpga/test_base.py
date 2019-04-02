# Copyright 2018 Intel, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock
import os
import subprocess

import fixtures

from cyborg.accelerator.drivers.fpga.base import FPGADriver
from cyborg.accelerator.drivers.fpga.intel import sysinfo
from cyborg.tests import base
from cyborg.tests.unit.accelerator.drivers.fpga.intel import prepare_test_data


class TestFPGADriver(base.TestCase):
    def test_create(self):
        FPGADriver.create("intel")
        self.assertRaises(LookupError, FPGADriver.create, "xilinx")

    def test_discover(self):
        d = FPGADriver()
        self.assertRaises(NotImplementedError, d.discover)

    def test_program(self):
        d = FPGADriver()
        self.assertRaises(NotImplementedError, d.program, "path", "image")
