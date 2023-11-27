# https://stackoverflow.com/questions/7628036/how-much-days-left-from-today-to-given-date
import datetime

today = datetime.date.today()
future = datetime.date(2024,1,1)
diff = future - today
print (diff.days)