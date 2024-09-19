from datetime import datetime, timedelta

hj = datetime.today()

print("hora: " + hj.strftime("%H:%M:%S"))
print("Data: " + hj.strftime("%d/%m/%y"))

print("Data + 2 dias: " + str(hj + timedelta(days=2)))
print("Data - 2 meses: " + str(hj + timedelta(days=60)))

dat = datetime.fromisoformat("2020-03-30T12:30:20")

dif = hj - dat
print(dif.days)