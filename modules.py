import datetime
import subprocess
CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''
def find_today_condition(soup):
    today_time_and_condition = soup.find(class_='fc_hours fc_hour_ratings').find_all('li')
    today_time_and_condition_dict = {}

    for time in today_time_and_condition:
        time_splitted = time.get_text().split(" ")
        today_time_and_condition_dict[int(time_splitted[1])] = time_splitted[2]

    return today_time_and_condition_dict

def astro_dark_duration(soup):
    details = soup.find(class_='fc_daylight').text.split(". ")
    astro_dark = details[-1][12:].split(" - ")

    start = astro_dark[0]
    start_hh = datetime.datetime.strptime(start, '%H:%M').hour

    end = astro_dark[1]
    end_hh = datetime.datetime.strptime(end, '%H:%M').hour

    return start_hh, end_hh

def find_good_hours(start_hh, end_hh, today_condition_dict, condition):
    midnight = False
    good_hours = 0
    max_consecutive_hours = 0
    consecutive_hours = 0
    start_hours = 0
    max_start_hours = 0

    for key, value in today_condition_dict.items():
        if key == 0:
            midnight = True

        if midnight:
            key += 24

        if start_hh <= key <= end_hh + 24:
            if value == condition:
                good_hours += 1
                consecutive_hours += 1
                if consecutive_hours == 1:
                    start_hours = key
                if consecutive_hours > max_consecutive_hours:
                    max_consecutive_hours = consecutive_hours
                    max_start_hours = start_hours if start_hours < 24 else start_hours - 24

            else:
                consecutive_hours = 0
    return good_hours, max_consecutive_hours, max_start_hours

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

def push_notifications(total_clear_hours, consecutive_hours, consecutive_hours_start, condition, clear_hours_threshold):
    if total_clear_hours >= clear_hours_threshold:
        notify("Clear skies tonight!", f"{condition} condition hours: {total_clear_hours}\nMaximum {consecutive_hours} consecutive hours from {consecutive_hours_start}:00")
        
        
