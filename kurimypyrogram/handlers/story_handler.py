#  kurimypyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of kurimypyrogram.
#
#  kurimypyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  kurimypyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with kurimypyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Callable

from .handler import Handler


class StoryHandler(Handler):
    """The Story handler class. Used to handle new stories.
    It is intended to be used with :meth:`~kurimypyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~kurimypyrogram.Client.on_story` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new Stories arrives. It takes *(client, story)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of stories to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~kurimypyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the story handler.

        story (:obj:`~kurimypyrogram.types.Story`):
            The received story.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
