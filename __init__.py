import os
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv


# This is an app that will display a big button that you click on to move everything on your D2 character to your vault
# Onslaught good, but drops a lot of loot. I just want it gone from my inventory


load_dotenv()

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://mightymatias.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token/"
get_user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_link = session.authorization_url(base_auth_url)
print(f"Auth link: {auth_link[0]}")

redirect_response = input("Paste your redirect url with query params here: ")

session.fetch_token(
    client_id=client_id,
    client_secret=client_secret,
    token_url=token_url,
    authorization_response=redirect_response
)

additional_headers = {"X-API-Key": os.getenv('API_KEY')}
response = session.get(url=get_user_details_endpoint, headers=additional_headers)

print(f"RESPONSE STATUS: {response.status_code}")
print(f"RESPONSE STATUS: {response.reason}")
print(f"RESPONSE TEXT: \n{response.text}")