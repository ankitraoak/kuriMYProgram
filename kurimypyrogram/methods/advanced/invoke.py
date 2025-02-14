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

import logging

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram.raw.core import TLObject
from kurimypyrogram.session import Session
from kurimypyrogram.methods.messages.business_session import get_session

log = logging.getLogger(__name__)


class Invoke:
    async def invoke(
        self: "kurimypyrogram.Client",
        query: TLObject,
        retries: int = Session.MAX_RETRIES,
        timeout: float = Session.WAIT_TIMEOUT,
        sleep_threshold: float = None,
        business_connection_id: str = None
    ):
        """Invoke raw Telegram functions.

        This method makes it possible to manually call every single Telegram API method in a low-level manner.
        Available functions are listed in the :obj:`functions <kurimypyrogram.api.functions>` package and may accept compound
        data types from :obj:`types <kurimypyrogram.api.types>` as well as bare types such as ``int``, ``str``, etc...

        .. note::

            This is a utility method intended to be used **only** when working with raw
            :obj:`functions <kurimypyrogram.api.functions>` (i.e: a Telegram API method you wish to use which is not
            available yet in the Client class as an easy-to-use method).

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            query (``RawFunction``):
                The API Schema function filled with proper arguments.

            retries (``int``):
                Number of retries.

            timeout (``float``):
                Timeout in seconds.

            sleep_threshold (``float``):
                Sleep threshold in seconds.

            business_connection_id (``str``, *optional*):
                Unique identifier of the business connection.

        Returns:
            ``RawType``: The raw type response generated by the query.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        if not self.is_connected:
            raise ConnectionError("Client has not been started yet")

        session = self.session

        if business_connection_id:
            query = raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=query
            )

            session = await get_session(self, business_connection_id)

        if self.no_updates:
            query = raw.functions.InvokeWithoutUpdates(query=query)

        if self.takeout_id:
            query = raw.functions.InvokeWithTakeout(takeout_id=self.takeout_id, query=query)

        r = await session.invoke(
            query, retries, timeout,
            (sleep_threshold
             if sleep_threshold is not None
             else self.sleep_threshold)
        )

        await self.fetch_peers(getattr(r, "users", []))
        await self.fetch_peers(getattr(r, "chats", []))

        return r
