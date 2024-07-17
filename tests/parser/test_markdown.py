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

import kurimypyrogram
from kurimypyrogram.parser.markdown import Markdown


# expected: the expected unparsed Markdown
# text: original text without entities
# entities: message entities coming from the server

def test_markdown_unparse_bold():
    expected = "**bold**"
    text = "bold"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.BOLD, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_italic():
    expected = "__italic__"
    text = "italic"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.ITALIC, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_strike():
    expected = "~~strike~~"
    text = "strike"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.STRIKETHROUGH, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_spoiler():
    expected = "||spoiler||"
    text = "spoiler"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.SPOILER, offset=0, length=7)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_url():
    expected = '[URL](https://kurimypyrogram.org/)'
    text = "URL"
    entities = kurimypyrogram.types.List([kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.TEXT_LINK,
                                                                 offset=0, length=3, url='https://kurimypyrogram.org/')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_emoji():
    expected = '![🥲](tg://emoji?id=5195264424893488796) im crying'
    text = "🥲 im crying"
    entities = kurimypyrogram.types.List([kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.CUSTOM_EMOJI,
                                                                 offset=0, length=2, custom_emoji_id=5195264424893488796)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_code():
    expected = '`code`'
    text = "code"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.CODE, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_pre():
    expected = """```python
for i in range(10):
    print(i)
```"""

    text = """for i in range(10):
    print(i)"""

    entities = kurimypyrogram.types.List([kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.PRE, offset=0,
                                                                 length=32, language='python')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_blockquote():
    expected = """> Hello
> from

> kurimypyrogram!"""

    text = """Hello\nfrom\n\nkurimypyrogram!"""

    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.BLOCKQUOTE, offset=0, length=10),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.BLOCKQUOTE, offset=12, length=9)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_mixed():
    expected = "**aaaaaaa__aaabbb**__~~dddddddd||ddeee~~||||eeeeeeefff||ffff`fffggggggg`ggghhhhhhhhhh"
    text = "aaaaaaaaaabbbddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh"
    entities = kurimypyrogram.types.List(
        [kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.BOLD, offset=0, length=13),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.ITALIC, offset=7, length=6),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.STRIKETHROUGH, offset=13, length=13),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.SPOILER, offset=21, length=5),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.SPOILER, offset=26, length=10),
         kurimypyrogram.types.MessageEntity(type=kurimypyrogram.enums.MessageEntityType.CODE, offset=40, length=10)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_no_entities():
    expected = "text"
    text = "text"
    entities = []

    assert Markdown.unparse(text=text, entities=entities) == expected
