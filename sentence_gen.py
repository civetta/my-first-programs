#The user inputs a number and the computer randomly generates that many sentences

def sentence_gen(n):
	import random
	n=int(n)
	count=0
	verbs=["ran ", "swam ", "threw "]
	nouns=["Billy ", "Sally ", "Betty "]
	direct_objects=["ball ", "cat ", "dog "]
	indirect_objects=["Billy. ", "Sally. ", "Betty. "]
	while count<n:
	        answer=random.choice(nouns)+random.choice(verbs)+"the "+random.choice(direct_objects)+"to "+random.choice(indirect_objects)
		count=count+1
		print answer
	return ""
	

print "Hello, this is a random sentence generator. How many sentences would you like generated?"
n=input()
print sentence_gen(n)