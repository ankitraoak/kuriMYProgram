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

from typing import Union

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram import types


class GetChatInviteLink:
    async def get_chat_invite_link(
        self: "kurimypyrogram.Client",
        chat_id: Union[int, str],
        invite_link: str,
    ) -> "types.ChatInviteLink":
        """Get detailed information about a chat invite link.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (str):
                The invite link.

        Returns:
            :obj:`~kurimypyrogram.types.ChatInviteLink`: On success, the invite link is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetExportedChatInvite(
                peer=await self.resolve_peer(chat_id),
                link=invite_link
            )
        )

        users = {i.id: i for i in r.users}

        return types.ChatInviteLink._parse(self, r.invite, users)
