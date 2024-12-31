#!/usr/bin/env python

import json
import atproto

with open("/opt/service/secret/dev.json", "r") as creds_file:
    creds = json.load(creds_file)

client = atproto.Client("https://dev.unifist.social/")
profile = client.login(creds["handle"], creds["password"])
print('Welcome,', profile.display_name)

text = atproto.client_utils.TextBuilder().text('Hello World from ').link('Python SDK', 'https://atproto.blue')
post = client.send_post(text)
client.like(post.uri, post.cid)
