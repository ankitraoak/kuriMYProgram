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

from uuid import uuid4

import kurimypyrogram
from kurimypyrogram import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedAudio`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedDocument`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedAnimation`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedPhoto`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedSticker`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedVideo`
    - :obj:`~kurimypyrogram.types.InlineQueryResultCachedVoice`
    - :obj:`~kurimypyrogram.types.InlineQueryResultArticle`
    - :obj:`~kurimypyrogram.types.InlineQueryResultAudio`
    - :obj:`~kurimypyrogram.types.InlineQueryResultContact`
    - :obj:`~kurimypyrogram.types.InlineQueryResultDocument`
    - :obj:`~kurimypyrogram.types.InlineQueryResultAnimation`
    - :obj:`~kurimypyrogram.types.InlineQueryResultLocation`
    - :obj:`~kurimypyrogram.types.InlineQueryResultPhoto`
    - :obj:`~kurimypyrogram.types.InlineQueryResultVenue`
    - :obj:`~kurimypyrogram.types.InlineQueryResultVideo`
    - :obj:`~kurimypyrogram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "kurimypyrogram.Client"):
        pass
