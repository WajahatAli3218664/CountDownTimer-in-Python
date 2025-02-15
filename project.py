#Project 5: Count Down Timer In Python
#Description: This is a countdown timer that takes time input from the user in seconds and then displays it in a minute:second format
#Instructor: Wajahat Ali

import time
def countdown_timer(time_in_seconds):
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_in_seconds -= 1
    print("00:00 \n Time's up!")
total_seconds = int(input("Enter the time in seconds for countdown: "))
countdown_timer(total_seconds)



