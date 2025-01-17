import json
import base64
import requests

class API:

    def __init__(self):

        with open("/opt/service/secret/zoom.json", "r") as creds_file:

            creds = json.load(creds_file)

            auth = base64.b64encode(bytes(f"{creds['client_id']}:{creds['client_secret']}", 'utf-8')).decode('utf-8')
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {auth}"
            }
            body = {
                "grant_type": "account_credentials",
                "account_id": creds['account_id']
            }

            response = requests.post("https://zoom.us/oauth/token", headers=headers, data=body)

            self.session = requests.Session()
            self.session.headers.update({"Authorization": f"Bearer {response.json()['access_token']}"})
