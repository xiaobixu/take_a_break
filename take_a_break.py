import webbrowser
import time

total_breaks = 5
curent_break = 1

print("Program starts at " + time.ctime())
while (curent_break <= total_breaks):
    time.sleep(10)
    webbrowser.open ("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    curent_break = curent_break + 1


