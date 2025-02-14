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

from kurimypyrogram import raw
from .auto_name import AutoName


class SentCodeType(AutoName):
    """Sent code type enumeration used in :obj:`~kurimypyrogram.types.SentCode`."""

    APP = raw.types.auth.SentCodeTypeApp
    "The code was sent through the telegram app."

    CALL = raw.types.auth.SentCodeTypeCall
    "The code will be sent via a phone call. A synthesized voice will tell the user which verification code to input."

    FLASH_CALL = raw.types.auth.SentCodeTypeFlashCall
    "The code will be sent via a flash phone call, that will be closed immediately."

    MISSED_CALL = raw.types.auth.SentCodeTypeMissedCall
    "Missed call."

    SMS = raw.types.auth.SentCodeTypeSms
    "The code was sent via SMS."

    FRAGMENT_SMS = raw.types.auth.SentCodeTypeFragmentSms
    "The code was sent via Fragment SMS."

    EMAIL_CODE = raw.types.auth.SentCodeTypeEmailCode
    "The code was sent via email."

    FIREBASE_SMS = raw.types.auth.SentCodeTypeFirebaseSms
    "The code should be delivered via SMS after Firebase attestation."

    SETUP_EMAIL_REQUIRED = raw.types.auth.SentCodeTypeSetUpEmailRequired
    "The user should add and verify an email address in order to login."

    SMS_PHRASE = raw.types.auth.SentCodeTypeSmsPhrase
    "The code was sent via SMS with a phrase."

    SMS_WORD = raw.types.auth.SentCodeTypeSmsWord
    "The code was sent via SMS with a word."
