import json
import requests
import os
from dotenv import load_dotenv

#load the API_KEY
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(title):
    res = requests.get("http://www.omdbapi.com/", params={"apikey": API_KEY, "t": title})
    return res.json()


