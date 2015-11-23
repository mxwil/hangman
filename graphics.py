from os import system

def clear():

	system("clear")

def drawgallows(x, score):

	clear()
	print 'Python Hangman v0.2\n\n'
	print 'Your score so far: %d' %(score)
	
	if x == 1:
		print '                 \n' * 6
		print '   _____        '
		return None
	elif x == 2:
		print '\n     |           ' * 6
		print '   __|__'
		return None
	else: 
		print '\n     |--------  '

	if x == 3:
		print '     | / '
	else:
		print '     | /     |  '


	if x == 4:
		print '     |'
	if x > 4 and x < 9:
		print '     |       o  ' 
	elif x == 9:
		print '     |       o/ ' 
	elif x ==10:
		print '     |      \o/ '


	if x > 5:
		print '     |       l  '
	else:
		print '     |          '

	if x == 7:
		print '     |      /   '
	elif x > 7: 
		print '     |      / \ '
	else:
		print '     |'

	print '     |          '
	print '   __|__        '

	if x == 10: 
		print '\n    GAME OVER \n'

	return None