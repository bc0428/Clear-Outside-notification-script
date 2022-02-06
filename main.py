#!/usr/bin/env python3
from modules import *
import requests
from bs4 import BeautifulSoup
import schedule
import time


# enter link of clearoutside with own location
# for example: "https://clearoutside.com/forecast/37.24/-115.79"
link = "YOUR LINK"

# condition could be set to find hours of Good / OK / Bad sky conditions
condition="Good"

# minimum hours of chosen conditions
condition_hours_threshold = 3






def main():
    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'html.parser')

    today_condition_dict = find_today_condition(soup)
    start_hh , end_hh = astro_dark_duration(soup)
    condition_hours, max_consecutive_hours, start_hours = find_good_hours(start_hh, end_hh, today_condition_dict, condition)

    push_notifications(condition_hours, max_consecutive_hours, start_hours, condition, condition_hours_threshold)

main()



