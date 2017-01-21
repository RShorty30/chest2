import random
from random import randint


n = randint(0,9)
def comparison(n):
	dates = []
	year = random.choice(range(2000, 2016))
	month = random.choice(range(1, 13))
	day = random.choice(range(1, 29))
	dates.append(str(month) + "/" + str(day) + "/" + str(year))
	for i in range(n-1):
		year -= 1
		month = random.choice(range(1, 13))
		day = random.choice(range(1, 29))
		dates.append(str(month) + "/" + str(day) + "/" + str(year))
	dates = (', '.join(map(str, dates)))
	print(dates)



comparison(n)



