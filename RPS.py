def rps():
	print "Welcome to my rock paper scissors games. It is played Best 2 out of 3"
	games,wins,loses,ties=0,0,0,0
	import random
	Answers={1:"ROCK",2:"PAPER",3:"SCISSORS"}
	while True:
		if wins==2:
			break
		if loses==2:
			break
		computer=random.randint(1,3)
		print "You've Won: "+str(wins)+" Times, Lost "+ str(loses)+ " times, and Tied "+ str(ties)+ " times"
		print "Pick (1)Rock,(2)Paper, or (3)Scissors!"
		user_in=raw_input()
		user_in=int(user_in)
		if user_in>3:
			print "Sorry that is in invalid statement"
			continue
		Computer=Answers[computer]
		User=Answers[user_in]
		if User==Computer:
			ties+=1
			print User + " vs " + Computer
			print "Tie"
		else:	
			games +=1
			if User=="ROCK" and Computer=="SCISSORS" or User=="SCISSORS" and Computer=="PAPER" or User=="PAPER" and Computer=="ROCK":
				print "You: "+ User + " vs " + " Computer: "+ Computer
				print "You Win!"
				wins += 1
			else:
				print "You: "+ User + " vs " + " Computer: "+ Computer
				print "You lost!"
				loses += 1
	print "Good Game, the final standing was, You: "+str(wins)+" Computer: "+str(loses)




print rps()
#1=Rock
#2=Paper
#3=Scissors