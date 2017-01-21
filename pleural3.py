import random
from random import randint
present = ["no", "a trace", "a small", "a moderate", "a large"]
size = ["no", "a trace", "a small", "a moderate", "a large"]
zize = ["no", "trace", "small", "moderate", "large"]
side = ["right", "left", "bilateral"]
greater = ["right greater than left ", "left greater than right ", ""]
file = open("Pleural Effusion3.txt", "w")
string_effusion = []


for p in present:
	for s in size:
		effusion = "There is " + p + " right pleural effusion. "
		effusion += "There is " + s + " left pleural effusion."
		string_effusion.append(effusion)

for z in zize:
	if z == "no":
		effusion = "There is no pleural effusion."
		string_effusion.append(effusion)
	for l in side:
		if l == "bilateral" and z != "no":
			for g in greater:
				effusion = "There are " + g + z + " bilateral pleural effusions."
				string_effusion.append(effusion)
		if l == "right" and z != "no":
			effusion = "There is a " + z + " right pleural effusion."
			string_effusion.append(effusion)
		if l == "left" and z != "no":
			effusion = "There is a " + z + " left pleural effusion."	
			string_effusion.append(effusion)

def random_effusion():
	return random.choice(string_effusion)

print(random_effusion())
order = '\n'.join(string_effusion)
file.write(order)