from datetime import datetime
dt=datetime.now()
print("Current date and time =",dt)

today=dt.strftime("%B %d,%Y %H : %M : %S")
print("current date and time =",today)