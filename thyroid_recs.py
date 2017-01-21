

def thyroid_nodule_recs(size, age):
	if age < 18:
		if size > 0:
			impression = "Recommend thyroid ultrasound for further evaluation if clinically indicated."
	if age >= 18 and < 35:
		if size >= 1:
			impression = "Recommend thyroid ultrasound for further evaluation if clinically indicated."
	if age >= 35:
		if size >= 1.5:
			impression = "Recommend thyroid ultrasound for further evaluation if clinically indicated."

