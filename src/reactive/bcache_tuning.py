#
# Copyright 2018 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import shutil
import subprocess
import os

from charms.reactive import when, when_not, set_flag

from charmhelpers.core.hookenv import status_set


@when_not('bcache-tuning.installed')
def install_bcache_tuning():
    shutil.copyfile('files/tune-bcache',
                    '/usr/local/bin/tune-bcache')
    os.chmod('/usr/local/bin/tune-bcache', 0o755)
    shutil.copyfile('files/tune-bcache.service',
                    '/lib/systemd/system/tune-bcache.service')
    subprocess.check_call(['systemctl', 'daemon-reload'])
    subprocess.check_call(['systemctl', 'enable',
                           'tune-bcache.service'])
    subprocess.check_call(['systemctl', 'start',
                           'tune-bcache.service'])
    set_flag('bcache-tuning.installed')


@when('bcache-tuning.installed')
def assess_status():
    status_set('active', 'bcache devices tuned')
