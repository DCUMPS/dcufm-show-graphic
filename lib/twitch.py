#!/usr/bin/env python3

import requests 
from bs4 import BeautifulSoup

def get_show_name(twitch_url):
  URL = twitch_url
  headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"} 
  r = requests.get(url=URL, headers=headers) 
  soup = BeautifulSoup(r.content, 'html5lib')

  meta_tag = soup.find('meta', {'property': 'og:description'})
  content = meta_tag.get('content')

  return content.strip()