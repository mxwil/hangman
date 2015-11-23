from os import system

def clear():

	system("clear")

def drawgallows(x, score):

	clear()
	print 'Python Hangman v0.2\n\n'
	print 'Your score so far: %d' %(score)
	
	if x == 1:
		print '                '
		print '                '
		print '                '
		print '                '
		print '                '
		print '                '
		print '   _____        '
	elif x == 2:
		print '     |          '
		print '     |          '
		print '     |          '
		print '     |          '
		print '     |          '
		print '     |          '
		print '   __|__        '
	elif x == 3:
		print '     |--------  '
		print '     | /        '
		print '     |          '
		print '     |          '
		print '     |          '
		print '     |          '
		print '   __|__        '
	elif x == 4:
		print '     |--------  '
		print '     | /     |  '
		print '     |          '
		print '     |          '
		print '     |          '
		print '     |          '
		print '   __|__        '
	elif x == 5:
		print '     |--------  '
		print '     | /     |  '
		print '     |       o  '
		print '     |          '
		print '     |          '
		print '     |          '
		print '   __|__        '
	elif x == 6:
		print '     |--------  '
		print '     | /     |  '
		print '     |       o  '
		print '     |       l  '
		print '     |          '
		print '     |          '
		print '   __|__        '
	elif x == 7:
		print '     |--------  '
		print '     | /     |  '
		print '     |       o  '
		print '     |       l  '
		print '     |      /   '
		print '     |          '
		print '   __|__        '
	elif x == 8:
		print '     |--------  '
		print '     | /     |  '
		print '     |       o  '
		print '     |       l  '
		print '     |      / \ '
		print '     |          '
		print '   __|__        '
	elif x == 9:
		print '     |--------  '
		print '     | /     |  '
		print '     |       o/ '
		print '     |       l  '
		print '     |      / \ '
		print '     |          '
		print '   __|__        '
	elif x == 10:
		print '     |--------  '
		print '     | /     |  '
		print '     |      \o/ '
		print '     |       l  '
		print '     |      / \ '
		print '     |          '
		print '   __|__        '
		print ''
		print '    GAME OVER   '