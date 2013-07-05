#The purpose of this is to take a number and it's measurement unit and convert it to the second measurement unit given

#------------------
#MAIN CONVERTER#
#------------------

def converter (num, original_unit,new_unit):
  #converts the number into float numbers, meaning they can have decimals which is good with conversions
  num=float(num)
  
  #the second set of libraries (dictionaries) that are organized by the first unit and contain links to the methods for converting to each of the other units
  conv_cup={'teaspoons':cup_tea, 'tablespoon':cup_table, 'cup':cup_cup, 'pint':cup_pint,'quart': cup_quart, 'gallon': cups_gallon}

  conv_teaspoon={'teaspoon':tea_tea,'cups':tea_cup, "tablespoon":tea_table,'pint': tea_pint, "quart": tea_quart, "gallon": tea_gallon}

  conv_tablespoon={'teaspoon':table_tea,'tablespoon':table_table,"cup":table_cup,"pint":table_pint,"quart":table_quart,"gallon":table_gallon}

  conv_pint={'teaspoon':pint_tea,'tablespoon':pint_table,'cup':pint_cup,'pint':pint_pint,'quart':pint_quart, 'gallon':pint_gallon}

  conv_quart={'teaspoon':quart_tea,'tablespoon':quart_table,'cup':quart_cup,'pint':quart_pint,'quart':quart_quart, 'gallon':pint_gallon}

  conv_gallon={'teaspoon':gall_tea,'tablespoon':gall_table,'cup':gall_cup,'pint':gall_pint,'quart':gall_quart, 'gallon':gall_gallon}

  #the first library (dictionary) which takes the original unit and calls upon one of the above libraries(dictionaries) that call upon the functions to convert to the new unit
  dic_con={'cup':conv_cup, 'teaspoon':conv_teaspoon, "tablespoon":conv_tablespoon, "pint":conv_pint, "quart":conv_quart, "gallon":conv_gallon }
  
#--------------------------------------------------------------------------------------------------------------------------------------#
# PIECE OF CODE THAT PULLS FROM FIRST LIBRARY WHICH "BOOK" TO USE TO CALL UPON THE FUNCTION THAT CONVERTS ORIGINAL UNIT INTO NEW UNIT
#--------------------------------------------------------------------------------------------------------------------------------------#

  #this piece of code use the .get to pull the "books" from the first library(dictionary), using the original_unit as the "keyword finder" thing
  library_2= dic_con.get(original_unit, None)
  #checks to see if the library even exists with the None above, if it does exist...
  if library_2 is not None:
    #pulls the function from the second library(dictionary)
    func=library_2.get(new_unit,None)
    if func is not None:
      #Runs the function
      return func(num)







#-----------------------------------------
# FUNCTIONS STARTING WITH TEASPOON UNIT#
#-----------------------------------------

#Teaspoons to Teaspoons
def tea_tea(n):
  return n

#Teaspoons into Tablespoons
def tea_table(n):
  return n/9

#Teaspoons into Cups
def tea_cup(n):
  return n/48

#Teaspoons into Pints
def tea_pint(n):
  return n/(48*2)

#Teaspoons into Quarts:
def tea_quart(n):
  return n/(48*4)

#Teaspoons into Galloons
def tea_gallon(n):
  return n/((48*4)*4)



#-------------------------------------------
# FUNCTIONS STARTING WITH TABLESPOON UNIT#
#-------------------------------------------
#Tablespoon to Teaspoon
def table_tea(n):
  return n*9

#Tablespoon to Tablespoon
def table_table(n):
  return n

#Tablespoons to Cups
def table_cup(n):
  return n/16

#Tablespoons to Pins
def table_pint(n):
  return n/32

#Tablespoons to Quart
def table_quart(n):
  return n/64

#Tablespoon to Gallon
def table_gallon(n):
  return n/(64*4)



#-------------------------------------------
# FUNCTIONS STARTING WITH CUP UNIT#
#-------------------------------------------

#Cup to Teaspoons
def cup_tea(n):
  return n*48

#Cups to Tablespoons
def cup_table(n):
  return n*16

#Cups to Cups
def cup_cup(n):
  return n

#Cups to Pints:
def cup_pint(n):
  return n/2

#Cups to Quarts:
def cup_quart(n):
  return n/4

#Cups to Gallon:
def cups_gallon(n):
  return n/8



#-------------------------------------------
# FUNCTIONS STARTING WITH PINT UNIT#
#-------------------------------------------

#Pint to Teaspoons
def pint_tea(n):
  return n*96

#Pint to Tablespoons
def pint_table(n):
  return n*32

#Pint into Cups
def pint_cup(n):
  return n*2

#Pint into Pints
def pint_pint(n):
  return n

#Pint into Quarts:
def pint_quart(n):
  return n/2

#Pint into Galloons
def pint_gallon(n):
  return n/8




#-------------------------------------------
# FUNCTIONS STARTING WITH QUART UNIT#
#-------------------------------------------

#Quart to Teaspoons
def quart_tea(n):
  return n*192

#Quart to Tablespoons
def quart_table(n):
  return n*64

#Quart into Cups
def quart_cup(n):
  return n*4

#Quart into Pints
def quart_pint(n):
  return n*2

#Quart into Quarts:
def quart_quart(n):
  return n

#Quart into Galloons
def quart_gallon(n):
  return n/2


#-------------------------------------------
# FUNCTIONS STARTING WITH GALLON UNIT#
#-------------------------------------------

#Gallon to Teaspoons
def gall_tea(n):
  return n*768

#Gallon to Tablespoons
def gall_table(n):
  return n*256

#Gallon into Cups
def gall_cup(n):
  return n*16

#Gallon into Pints
def gall_pint(n):
  return n*8

#Gallon into Quarts:
def gall_quart(n):
  return n*4

#Gallon into Galloons
def gall_gallon(n):
  return n




#INPUT METHODS
input_num=raw_input('Whats your number? ')
input_original_unit=raw_input('Original Unit? ')
input_new_unit=raw_input('New Unit? ')

output=converter(input_num,input_original_unit, input_new_unit) 
print "There are %s %ss in %s %ss." %(str(output),input_new_unit, input_num, input_original_unit)

