"""A guessing game where the computer randomly generates a number and the user tries to guess that number. If the number is too high it returns "Too High", if it's lower then the randomly generate number it returns "Too Low". It keeps going until the user gets it. It then returns the number of tries it took for the user to get it."""
import random
number= random.randint(1,10)
guessTaken = 0
print "Hello, I am thinking of a number between 1-10. Can you guess what it is?"
guess=0
while guess != number:
	guess=input()
	guess=int(guess)
	guessTaken=guessTaken+1
	if guess > number:
		print "Too High"
	if guess <number:
		print "Too Low"
	if guess ==number:
		guessTaken=str(guessTaken)
		print "Good Job, it took you " +guessTaken+" guesses to get that!"
