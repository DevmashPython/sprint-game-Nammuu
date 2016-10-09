import msvcrt

finish=10
count1=count2=count3=0

print "press enter key to get started"
raw_input()

while count1!=10:
	key=msvcrt.getch()
	if key=='d':
		count1=count1+1
		print "_",
	else:
		print "error"
		exit()

if count1==10:
	print "\n"
while count2!=10:
	key=msvcrt.getch()
	if key=='s':
		count2=count2+1
		print "                    |"
	else:
		print "error"
		exit()

if count2==10 and count1==10:
	print "                    ",
while count3!=finish:
	key=msvcrt.getch()
	if key=='d':
		count3=count3+1
		print "_",
	else:
		print "error"
		break
print "congrats"			

'''
1. Mention controls for the game.
2. Mention when to turn right and when to turn down.	
'''
