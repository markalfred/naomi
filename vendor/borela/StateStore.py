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


class StateStore:
    """
    Represents a container for the application’s state that can be changed by
    applying events to it.
    """

    def __init__(self, **reducers):
        self.__reducers = reducers
        self.__state = {}

        # Initialize state.
        for name, reducer in reducers.items():
            self.__state[name] = reducer()

    def __contains__(self, key):
        return key in self.__state

    def __getitem__(self, key):
        return self.__state[key]

    def __iter__(self):
        return iter(self.__state)

    def __len__(self):
        return len(self.__state)

    def apply(self, event):
        event_type = event.get('type', None)

        if not isinstance(event_type, str):
            raise ValueError('Invalid event type.')

        for name, reducer in self.__reducers.items():
            old_state = self.__state[name]
            self.__state[name] = reducer(old_state, event)

    @property
    def state(self):
        return self.__state

    @property
    def reducers(self):
        return self.__reducers