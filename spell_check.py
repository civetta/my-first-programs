def spell_check(n):
  #Declaring variables and preparing the string to alter
  mispelled_word=[]
  dictionary = open("DictionaryE.txt").readlines()
  str=n.lower().split()
  str=list(str)
  for i in range (len(dictionary)):
    dictionary[i]=dictionary[i].strip()
  for e in str:
     if e not in dictionary:
          mispelled_word.append(e)
          continue
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