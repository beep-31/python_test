import random 
guess = ''
user_input = ''
responses = ['Bad luck', 'Try one more time', 'Not your day buddy']
while user_input != 'quit':
	user_input = input(str("Eagle or tails?"))
	toss = random.randint(0,1) #0-eagle 1-tails
	if toss == 0 and user_input.lower() == "eagle" or toss == 1 and user_input.lower()=='tails':
		print("YES! THAT'S RIGHT!\n")
	else:
		print(responses[random.randint(0,len(responses)-1)] + "\n")