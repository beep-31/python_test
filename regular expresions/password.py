import re

while True:
	points = 0
	password = input(str(">> Write down your password: "))
	if password.lower() == 'quit':
		break
	else:
		if len(password) >= 8:
			points = points + 1
		if re.search("[a-z]", password):
			points = points + 1
		if re.search("[A-Z]", password):
			points = points + 1
		if re.search("[0-9]", password):
			points = points + 1

	if points > 2:
		print("Strong password")
	else: 
		print("Weak password")