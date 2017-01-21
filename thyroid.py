import random
from random import randint
import numpy as np
present = ["no", "a trace", "a small", "a moderate", "a large"]
size = np.arange(0, 3.1, 0.1)
side = ["right", "left"]
file = open("thyroid_nodule.txt", "w")
string_thyroid_nodule = []

for s in size:
	s = str(s)
	if s == "0.0":
		nodule = "The thyroid is normal."
		string_thyroid_nodule.append(nodule)
	else:
		for l in side:
			nodule = "There is a " + s + " cm nodule in the " + l + " lobe of the thyroid gland." 
			string_thyroid_nodule.append(nodule)

def random_thyroid_nodule():
	return random.choice(string_thyroid_nodule)

print(random_thyroid_nodule())
order = '\n'.join(string_thyroid_nodule)
file.write(order)