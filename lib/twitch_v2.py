#!/usr/bin/env python3

import requests 
from bs4 import BeautifulSoup

def get_show_name_v2(twitch_url):
  try:
    URL = twitch_url
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"} 
    r = requests.get(url=URL, headers=headers) 
    soup = BeautifulSoup(r.content, 'html5lib')
    
    first_script = soup.find_all('script')[0]
    script_description = first_script.string
    script_description = script_description.split('"description":"')[1]
    script_description = script_description.split('"')[0]

    return script_description.strip()
  except Exception as e:
    return "You're listening to DCUfm!"
