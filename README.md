# Clear-Outside-notification-Script
Creates pop-up notification when it is forecasted to have the desired sky conditions during "Astro-dark" time.
![Screenshot 2022-02-06 at 5 46 06 PM](https://user-images.githubusercontent.com/71583394/152676503-3b3bf3f9-b468-43ae-95b6-8012c5c11aad.png)</br></br></br>

# Background
The motivation of creating this script is to ease the pain of Astronomers and Astrophotographers from constantly checking sky conditions, especially in tropical and humid areas. This script scraps sky condition infomation from [Clear Ouside](https://clearoutside.com/forecast/50.7/-3.52) and creates pop-up notification on Mac</br></br></br>

# Installation
The scipt itself is executed in main.py and all necesary functions are in modules.py

It was designed to perform in association with crontab on Mac such that information can be acquired regularly, the scipt itself obtains information once per run.

For example, 
open crontab from terminal and add the scheduling,
```
crontab -e
* * * * * <path to python executables> <path of main.py>
```
more can be found [here](https://www.adminschoice.com/crontab-quick-reference)</br></br></br>

# Customisation

In main.py, one should define:
1. their location by assigning the Clear Outside site with own location to the "link" variable.</br>
2. the desired sky condition, which could be "Good", "OK" and "Bad" as defined by Clear Ouside.</br>
3. minimum hours of selected conditions to get notifications (in total, not consecutive hours)
