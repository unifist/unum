#!/usr/bin/env python

import json
import zoom

zoom_client = zoom.API()
print(json.dumps(zoom_client.session.get("https://api.zoom.us/v2/meetings/meeting_summaries").json(), indent=2, sort_keys=True))

meeting_id = zoom_client.session.get("https://api.zoom.us/v2/meetings/meeting_summaries").json()["summaries"][0]["meeting_uuid"]

print(meeting_id)

print(json.dumps(zoom_client.session.get(f"https://api.zoom.us/v2/meetings/{meeting_id}/meeting_summary").json(), indent=2, sort_keys=True))

print(json.dumps(zoom_client.session.get(f"https://api.zoom.us/v2/meetings/{meeting_id}/recordings").json(), indent=2, sort_keys=True))
