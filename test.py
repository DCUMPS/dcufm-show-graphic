#!/usr/bin/env python3

import random
import time
from datetime import datetime, timedelta
from lib.obs_image import create_obs_image
from lib.twitch import get_show_name
from lib.twitch_v2 import get_show_name_v2
from lib.twitch_v3 import get_twitch_channel_info
from config import *

show_name = get_show_name_v2("https://www.twitch.tv/dcufm")
create_obs_image(show_name)

print(get_twitch_channel_info(broadcaster_id, client_id, client_secret))
