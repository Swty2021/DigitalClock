#Digital Clock
import sys, time
import sevseg #imports sevseg.py

try:
    while True: #Main program loop
        print('\n' * 60) #Clear the screen by printing several new lines

        #Get current system time
        current_time = time.localtime()
        # %12 for 12 hour clock not 24
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours == '12' #12-hours clock time 12:00 not 00:00
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        #Get Digit strings from sevseg module
        hour_digits = sevseg.getSevSegStr(hours, 2)
        hour_TopRow, hour_MiddleRow, hour_BottomRow = hour_digits.splitlines()

        minute_digits = sevseg.getSevSegStr(minutes, 2)
        minutes_TopRow, minutes_MiddleRow, minutes_BottomRow = minute_digits.splitlines()

        second_digits = sevseg.getSevSegStr(seconds, 2)
        second_TopRow, second_MiddleRow, second_BottomRow = second_digits.splitlines()

        #Display the digits
        print(hour_TopRow + '  ' + minutes_TopRow + '  ' + second_TopRow)
        print(hour_MiddleRow + '  ' + minutes_MiddleRow + '  ' + second_MiddleRow)
        print(hour_BottomRow + '  ' + minutes_BottomRow + '  ' + second_BottomRow)
        print()
        print('Press Ctrl-C to quit.')

        #Keep looping until the second changes
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    print("Digital Clock")
    sys.exit() # When Ctrl-C is pressed, end the program

        
