from telethon.sync import TelegramClient
from telethon import errors
import sys

api_id = 11939332
api_hash = "8562fa6c0af2f9ebdea359008d5d4175"
phone = input('Enter phone (+62): ')

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except errors.SessionPasswordNeededError:
        client.sign_in(phone, password = input("Enter two-step password: "))
