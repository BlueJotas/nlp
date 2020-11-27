import json
import requests
from dotenv import load_dotenv
import os

def spotifyToken():

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    print(CLIENT_ID)
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET), verify=False) 

    token_raw = json.loads(response.text)
    token = token_raw['access_token']
    return token_raw