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

from typing import AsyncGenerator

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram import types
from kurimypyrogram import utils


class SearchPosts:
    async def search_posts(
        self: "kurimypyrogram.Client",
        hashtag: str,
        limit: int = 0,
    ) -> AsyncGenerator["types.Message", None]:
        """Search posts globally by hashtag.

        If you want to get the posts count only, see :meth:`~kurimypyrogram.Client.search_posts_count`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hashtag (``str``):
                Text query string.

            limit (``int``, *optional*):
                Limits the number of posts to be retrieved.
                By default, no limit is applied and all posts are returned.

        Returns:
            ``Generator``: A generator yielding :obj:`~kurimypyrogram.types.Message` objects.

        Example:
            .. code-block:: python

                # Search for "#kurimypyrogram". Get the first 50 results
                async for message in app.search_posts("#kurimypyrogram", limit=50):
                    print(message.text)
        """
        current = 0
        total = abs(limit) or (1 << 31)
        limit = min(100, total)

        offset_date = 0
        offset_peer = raw.types.InputPeerEmpty()
        offset_id = 0

        while True:
            messages = await utils.parse_messages(
                self,
                await self.invoke(
                    raw.functions.channels.SearchPosts(
                        hashtag=hashtag,
                        offset_rate=offset_date,
                        offset_peer=offset_peer,
                        offset_id=offset_id,
                        limit=limit
                    ),
                    sleep_threshold=60
                ),
                replies=0
            )

            if not messages:
                return

            last = messages[-1]

            offset_date = utils.datetime_to_timestamp(last.date)
            offset_peer = await self.resolve_peer(last.chat.id)
            offset_id = last.id

            for message in messages:
                yield message

                current += 1

                if current >= total:
                    return
