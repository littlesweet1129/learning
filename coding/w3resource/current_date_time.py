# Write a Python program to display the current date and time
import datetime as dt
# to get current date: dt.date.today()
# to get current date time: dt.datetime.now()
# once object is created, format with .strftime()
class Current():
    def __init__(self):
        pass
    def get_date_time(self):
        now = dt.datetime.now()
        print('Current date and time: ')
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

current = Current()
current.get_date_time()