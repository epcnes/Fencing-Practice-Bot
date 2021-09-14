from datetime import date, datetime, timedelta
dates = []

def tuesdays(year):
     d = date(year, 1, 12)
     d += timedelta(days = 2 - d.weekday())
     while d.year ==year:
          yield d 
          d += timedelta(days = 7)
for d in tuesdays(2022):
     d = d.strftime(f"{d}")
     dates.append(d)
f = open("days.py", "a")
f.write(f"\nwednesdays2022 = {dates}")

#DO NOT RUN FILE#
#EXAMPLE/REFERENCE FOR LATER ONLY#