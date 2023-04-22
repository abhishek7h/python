from datetime import datetime, date

now = datetime.now()
today = date.today()

current_time = now.strftime("%I:%M %p")
print("The time is", current_time)

to_day = today.strftime("%B %d, %Y")
print("Today is", to_day)

# if now < "12:00 PM":
#     print("Good morning!")
# elif now > "12:00 PM":
#     print("Good evening!")
