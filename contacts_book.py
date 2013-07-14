#The Purpose of this Program is to store addresses and allows the user to add more contact info, look up contact info, and edit contact info.
#----------------------------------------------------#	
#-----------------ADDRESS BOOK FUNCTIONS-------------#
#----------------------------------------------------#		
def add_address(title):
	print "Please enter a phone number"
	phone="Phone Number: "+ raw_input()
	address_info=[title,phone,'\n']
	with open('/home/civetta/my-first-programs/address.txt', 'a') as f:
		for e in address_info:
	    	    f.write(e+'\n')	
	return "Thank you for adding to your address book"
	


##LOOK UP FUNCTION##
def look_up(title):
	title=title+'\n'
	with open('/home/civetta/my-first-programs/address.txt') as f:
   		lines=f.readlines( )
   		if title not in lines:
			print "I'm sorry, that name is not in our address book. We are returning you to the main menu"
			main_menu()
		else:
			for i in range(2):
				print lines[lines.index(title)+i][:-1]
	print "Thanks!"

##THE EDIT FUNCTION##
def edit(title):
	print look_up(title)
	title=title+'\n'
	#If title matches, changer turns to True, if changer is True, changes happen then turned off.
	changer=False
	num,new_replace="",""
	with open('/home/civetta/my-first-programs/address.txt') as fin:
		with open('/home/civetta/my-first-programs/address2.txt',"w") as fout:
			print "What would you like to change? Type in one of the following numbers that correspond with what you would like to edit.'\n1  Name '\n2  Number"
			user_in=raw_input( )
	
			if user_in == "1":
				num=title
				print "You would like to change their name. Please type out their new name."
				new_replace=raw_input( )+''+'\n'
	
			if user_in=="2":
				num="Phone"
				print "You would like to change their number. Please type out their new number"
				new_replace="Phone: "+raw_input( )+'\n'
	

			for line in fin:
				if title==line:
					changer=True
				if changer==True and num in line:
						changer=False
						fout.write(line.replace(line,new_replace))
				else:
					fout.write(line)		
	copy_files(0)


#This function rewrite its to the original text file and then clears the second file
def copy_files(title):
	with open('/home/civetta/my-first-programs/address.txt','w') as fin:
		with open('/home/civetta/my-first-programs/address2.txt') as fout:
			for line in fout:
    					fin.write(line)
    #clears second file 					
	open('/home/civetta/my-first-programs/address2.txt',"w").close()	
	print "Thanks!"





#--------------------------------------------#	
#-----------------MENU FUNCTIONS-------------#
#--------------------------------------------#		

#The main menu function. Returned too often.
def main_menu():
	print """'\n' Hello, welcome to Kelly's Address Book Program. Please enter which action you would like to take.
Type 1 if you would like to ADD a new entry into your address book.
Type 2 if you would like to LOOK UP an entry you already have.
Type 3 if you would like to EDIT an entry you already have.
Type 4 if you would like to EXIT the program."""
	input=0
	while input != "4":
		input=raw_input( )
		if input=="1":
			print '\n'
			add_menu()
		if input =="2":
			print '\n'
			look_up_menu()
		if input =="3":
			print '\n'
			edit_menu()
		#If they type in exit, it ends the program with a return statement
		if input=="4":
			print '\n'
			print "Goodbye"
			import sys
			sys.exit()
		else:
			print "I do not understand what you said. Please try typing either 'Add' or 'Look'"
			continue
		

#The Look-Up Menu function. 
def look_up_menu():
	print "To look up an entry in your address book please type out the title of the entry, which is the First and Last name of the person you are searching for."
	while True:
		input=raw_input()
		print '\n'
		look_up(input)
		print "Would you like to look up another entry?(Y,N)"
		answer=raw_input( )
		if answer.upper()=="Y":
			print "Please enter the first and last of the person you'd like to look up"
			continue
		else:
			main_menu()

#The add menu function
def add_menu():
	print  "Please enter the first and last name of the person you'd like to add"
	while True:
		input=raw_input()
		add_address(input)
		print "Would you like to look up another entry?(Y,N)"
		answer=raw_input( )
		if answer.upper()=="Y":
			print "Please enter the name of the person you'd like to add"
			continue
		else:
			main_menu()
			return 


#The edit menu function
def edit_menu():
	print "Please type the full and last name of the person's entry you'd like to update"
	while True:
		checking=raw_input()
		edit(checking)
		print "Would you like to edit another entry?(Y,N)"
		answer=raw_input( )
		if answer.upper()=="Y":
			print "Please enter the name of the person you'd like to edit"
			continue
		else:
			main_menu()

	
###RUNS THE PROGRAM####
print main_menu()
