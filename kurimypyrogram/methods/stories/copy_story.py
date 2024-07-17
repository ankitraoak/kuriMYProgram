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
from typing import Union, List, Optional

import kurimypyrogram
from kurimypyrogram import types, enums

log = logging.getLogger(__name__)


class CopyStory:
    async def copy_story(
        self: "kurimypyrogram.Client",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        story_id: int,
        caption: str = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        period: int = None,
        privacy: "enums.StoriesPrivacyRules" = None,
        allowed_users: List[Union[int, str]] = None,
        disallowed_users: List[Union[int, str]] = None,
        protect_content: bool = None
    ) -> "types.Story":
        """Copy story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the source chat where the original message was sent.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_id (``int``):
                Message identifier in the chat specified in *from_chat_id*.

            caption (``string``, *optional*):
                New caption for story, 0-1024 characters after entities parsing.
                If not specified, the original caption is kept.
                Pass "" (empty string) to remove the caption.

            period (``int``, *optional*):
                How long the story will posted, in secs.
                only for premium users.

            privacy (:obj:`~kurimypyrogram.enums.StoriesPrivacyRules`, *optional*):
                Story privacy.
                Defaults to :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.PUBLIC`

            allowed_users (List of ``int`` | ``str``, *optional*):
                List of user_id or chat_id of chat users who are allowed to view stories.
                Note: chat_id available only with :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.SELECTED_USERS`.
                Works with :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.CLOSE_FRIENDS`
                and :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.SELECTED_USERS` only

            disallowed_users (List of ``int`` | ``str``, *optional*):
                List of user_id whos disallow to view the stories.
                Note: Works with :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.PUBLIC`
                and :obj:`~kurimypyrogram.enums.StoriesPrivacyRules.CONTACTS` only

            protect_content (``bool``, *optional*):
                Protects the contents of the sent story from forwarding and saving.

            parse_mode (:obj:`~kurimypyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~kurimypyrogram.types.MessageEntity`):
                List of special entities that appear in the new caption, which can be specified instead of *parse_mode*.

        Returns:
            :obj:`~kurimypyrogram.types.Story`: On success, the copied story is returned.

        Example:
            .. code-block:: python

                # Copy a story
                await app.copy_story(to_chat, from_chat, 123)

        """
        story: types.Story = await self.get_stories(from_chat_id, story_id)

        return await story.copy(
            chat_id=chat_id,
            caption=caption,
            period=period,
            protect_content=protect_content,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            privacy=privacy,
            allowed_users=allowed_users,
            disallowed_users=disallowed_users
        )
