import os
import random
import shutil

capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Pheonix', 'Arkansas':'Litle Rock',
 'California':'Sacramento','Colorado':'Denver', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu',
 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka',
 'Kentucky':'Frankfort', 'Montana':'Helena', 'New York': 'Albany', 'South Dakota':'Pierre', 'Utah':'Salt Lake City'}
cwd = os.getcwd()

if(os.path.exists(os.path.join(cwd, 'exam')) == False):
	os.mkdir('exam')
else:
	shutil.rmtree('exam')
	os.mkdir('exam')
	

for quizNum in range(3):
	# Create exam files and answer keys
	quizFile = open('exam\\capitalquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('exam\\capitalquiz_answers%s.txt' % (quizNum + 1), 'w')
	#Create the header of exam
	quizFile.write('Name:\n\nDate:\n\nCourse:\n\n')
	quizFile.write("\t\t\tStates' capitals exam. Ticket number %s" % (quizNum + 1))
	quizFile.write('\n\n')
	#Change order of the states
	states = list(capitals.keys())
	random.shuffle(states)
	#Create a loop for all states and ask a question for each one
	for questionNum in range(len(states)):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		quizFile.write('%s) Choose the capital of the state %s\n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
	