#!/usr/bin/python

import graphics, random

def chooseword(): #select a random word from a list of words 'dictionary.txt'

	try:
		f = open('dict.txt').read()
		w = [w.lower() for w in f.split('\n')]
	except IOError:
		print "**************************"
		print "Dictionary file not found!"
		print "**************************"
		while True:
			try:
				f = open(raw_input('Enter path to dictionary file:\n')).read()
				w = [w.lower() for w in f.split('\n')]
				break
			except IOError:
				print "Invalid file path entered!"

	return random.choice(w)

def fill_guessed(word, blanks, guessed): #function for filling the underscores with guessed letters

	spaced = ' '.join(list(word)) #create a list alternating the letters of the word and spaces
	out = list(blanks) # initialise an output as the dashes corresponding to word length
	chars = set(list(word)) # all unique letters
	for letter in guessed: #check each letter in guessed list, 
		if letter in chars: #if it's in the letter set,
			for i in range(0,len(spaced)): #replace all blanks corresponding to that letter with the letter itself
				if spaced[i] == letter:
					out[i] = letter

	return ''.join(out) #return the filled blanks as a string



def drawword(word, guessed):

	length = len(word)
	blanks = ' '.join(list('_'*len(word)))
	to_print = fill_guessed(word, blanks, guessed)
	print '\n',to_print,'\n'

def drawguessed(guessed):

	print 'Guessed letters:\n'
	print ' '.join(guessed)

def is_complete(word, guessed):

	letters = set(word)
	guessed_letters = set(guessed)
	number_of_letters = len(letters)

	matches = len([l for l in letters if l in guessed_letters]) #number of correctly guessed letters
	if matches == number_of_letters: #if all letters have been guessed
		return True
	else: return False

def response(result):

	if result == 0:
		return random.choice(['Your doom draws nearer!', 'Unlucky, the gallows beckon you ever closer...', 'Nope! MWAHAHAHA', 'That was a big mistake...', 'Keep guessing like this and I\'ll have your head!', 'It\'s almost as if you WANT to be hanged.','Better start preparing that last meal.','The birds will eat well tonight!', 'Come the morrow, your head will be on a pike!'])
	elif result == 1:
		return random.choice(['Good guess.', 'You\'re not too bad at this...','Aha, nicely done.','You may yet live...', 'How did you...?!','Grr, you may have got that one but I\'ll still have your head.','Good job, things aren\'t looking so bad for you after all!'])
	elif result == 2:
		return random.choice(['You win! Congratulations.', 'You win, good game!'])
	else: return ''


def turn(word, life, guessed, result, score):

	graphics.drawgallows(life, score)
	drawword(word, guessed)
	drawguessed(guessed)

	print '\n',response(result),'\n'

	if result == 2: 
		raw_input('Press [Enter] to start again.')
		return 4 #restart code

	if life < 10: #if user has lives remaining, 	
		if not is_complete(word, guessed): #if the word is not complete
			
			while True:
				guess = raw_input('Your next guess:\n').lower() #take the guess
				if (len(guess) == 1 and guess.isalpha()):
					break
				else:
					return 3
			
			if not guess in guessed: #if the guess is a new letter, add it to the guessed list
				guessed.append(guess)
			if guess in list(word): #if it's a correct guess, don't take a life
				return 1
			else: #else take a life off
				return 0
		else: #if word is complete, user wins (result code 2)
			return 2

	else:
		print 'You lose! The word was: %s' % (word)
		raw_input('Press [Enter] to start again.')
		return 4 #exit game loop

def main(score=0):
	while True:
		life = 1
		word = chooseword()
		guessed = []
		result = 5

		while not result == 4:
			result = turn(word,life, guessed, result, score)
			if result == 0:
				life += 1

		if life < 10: score += 1


			
if __name__ == '__main__':

	graphics.clear()
	print '\nWelcome to Python Hangman!'
	raw_input('\nPress [Enter] to begin.')

	main()