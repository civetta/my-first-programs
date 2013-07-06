def spell_check(n):
  #Declaring variables and opening the dictionary
  mispelled_word=[]
  dictionary = open("DictionaryE.txt").readlines()
  #Sending the string to all lower cases letters and seperating it into a list
  str=n.lower().split()
  str=list(str)
  #removing the commas or anything else from the string list
  for i in range(len(str)):
     str[i]=str[i].strip()
  #removing the return characters at the end of the list
  for i in range (len(dictionary)):
    dictionary[i]=dictionary[i].strip()
  #for each word in the sentence, if it's not in the dictionary then append it to the mispelled_word list
  for e in str:
     if e not in dictionary:
          mispelled_word.append(e)
          continue
  #run the list and using the jaccord coeffictient checks how close the words in the dictionary is compared to the mispelled word
  for e in mispelled_word:
    mispelled=e
    a=set(e)   
    for e in dictionary:
         dic_word=e
         if abs(len(dic_word)-len(mispelled))>4:
             continue
         else:
           b=set(e)
           jac = (float(len(a & b)) / float(len (a|b)))
           if len(mispelled)<3:
             if jac>.6:
               print dic_word
           else:
             if jac>.72:
               print dic_word
  

print spell_check("I lve my dg Alas")