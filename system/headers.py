# Licensed under the Apache License, Version 2.0 (the “License”); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from os.path import join
from .paths import HEADERS_DIR
from .fs import read_file


def command():
    return read_file(join(HEADERS_DIR, 'command.txt'))


def keymap():
    return read_file(join(HEADERS_DIR, 'keymap.txt'))


def menu():
    return read_file(join(HEADERS_DIR, 'menu.txt'))


def plist():
    return read_file(join(HEADERS_DIR, 'plist.txt'))


def preferences():
    return read_file(join(HEADERS_DIR, 'preferences.txt'))
