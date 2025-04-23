
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact
import pandas as pd

api_id = 25807311
api_hash = 'bec19e61265c2ec479c7f74b64ad89ce'
session_name = 'tg_number_checker'

df = pd.read_excel('number.xlsx')
numbers = df['phone'].dropna().astype(str).tolist()

with TelegramClient(session_name, api_id, api_hash) as client:
    contacts = []
    for idx, number in enumerate(numbers):
        contacts.append(InputPhoneContact(client_id=idx, phone=number, first_name="Test", last_name="User"))

    result = client(ImportContactsRequest(contacts))
    
    found_users = result.users
    print("\n--- Telegram Accounts Found ---")
    for user in found_users:
        print(f"{user.phone} | {user.first_name} {user.last_name} | @{user.username}")

    client(DeleteContactsRequest(id=found_users))
