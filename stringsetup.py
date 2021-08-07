#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """
STEP -1: Go-to my.telegram.org\n
STEP -2: sign up
STEP -3: tap on API Development Tools\n
STEP -4: copy get api_id and api_hash\n
STEP -5: come here & give those values here.\n\n
NOTE: If it asks to make app during sign in my.telegram.org then create the app and after creating you'll reach STEP -3, copy those values there.\n
"""
)


APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message(
        "me", 
        f"This is your catbot session:\n\n`{client.session.save()}`")
