###Make a list of the words in a text and sort it in Alphabetical Order

name=raw_input('Enter file name')
hand=open(name)
lst=list()
for line in hand:
 line=line.rstrip()
 aux=line.split()
  for word in aux:
   if word in lst: continue
   lst.append(word)
lst.sort()
print lst
hand.close()
