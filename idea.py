import json
import os

from hubspot3.contacts import ContactsClient
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUBSPOT_API_KEY")

client = ContactsClient(api_key=API_KEY)
contacts_data = client.get_all()

ids = []

for contact in contacts_data:
    ids.append(contact['id'])

jsonKeys = []
x = 0
frame = {}

for i in ids:
    with open('data/{}.json'.format(i)) as json_data:
        d = json.load(json_data)
        if x == 0:
            jsonKeys.append(list(d))
            frame[jsonKeys[0][x]] = d[list(d)[x]][0]
            x += 1
        else:
            for y in jsonKeys:
                frame[jsonKeys[0][y]] = d[list(d)[y]][0]   
            x += 1

print(frame)