#!/usr/bin/env python3

import random
import time
from datetime import datetime, timedelta
from lib.obs_image import create_obs_image
from lib.twitch import get_show_name


def main_loop():
    while True:
        current_time = datetime.now()

        start_time = current_time.replace(
            hour=9, minute=0, second=0, microsecond=0)
        end_time = current_time.replace(
            hour=20, minute=0, second=0, microsecond=0)
        is_weekday = current_time.weekday() < 5

        if is_weekday and start_time <= current_time <= end_time:
            try:
                show_name = get_show_name("https://www.twitch.tv/dcufm")
                create_obs_image(show_name)

                wait_time = random.randint(30, 45)
                time.sleep(wait_time)

            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")
                time.sleep(5)

        else:
            create_obs_image("No shows on at the moment")

            if current_time > end_time or not is_weekday:
                next_start_time = start_time + timedelta(days=1)
                while next_start_time.weekday() >= 5:
                    next_start_time += timedelta(days=1)
            else:
                next_start_time = start_time

            sleep_duration = (next_start_time - datetime.now()).total_seconds()
            print(
                f"No shows available. Sleeping for {sleep_duration / 3600:.2f} hours.")
            time.sleep(sleep_duration)


if __name__ == "__main__":
    while True:
        try:
            main_loop()
        except Exception as e:
            print(f"Critical error in main loop: {e}. Restarting...")
            time.sleep(5)
