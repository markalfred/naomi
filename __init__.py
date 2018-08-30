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

from Naomi.system.commands.BuildCommands import NaomiBuildCommandsCommand
from Naomi.system.commands.BuildIndentationPreferences import NaomiBuildIndentationPreferencesCommand
from Naomi.system.commands.BuildKeymaps import NaomiBuildKeymapsCommand
from Naomi.system.commands.BuildMenus import NaomiBuildMenusCommand
from Naomi.system.commands.RunCommands import NaomiRunCommandsCommand
from Naomi.system.commands.WatchCommands import NaomiWatchCommandsCommand
from Naomi.system.commands.WatchIndentationPreferences import NaomiWatchIndentationPreferencesCommand
from Naomi.system.commands.WatchKeymaps import NaomiWatchKeymapsCommand

__all__ = [
  NaomiBuildCommandsCommand,
  NaomiBuildIndentationPreferencesCommand,
  NaomiBuildKeymapsCommand,
  NaomiBuildMenusCommand,
  NaomiRunCommandsCommand,
  NaomiWatchCommandsCommand,
  NaomiWatchIndentationPreferencesCommand,
  NaomiWatchKeymapsCommand,
]
