#Finding who was the most prolific e-mailer

name=raw_input('Enter file name:')
hand=open(name)
dicio=dict()

###Counting ocurrences of wach sender
for line in hand:
  if not line.startswith('From: '): continue
  words=line.split()
  dicio[words[1]]=dicio.get(words[1],0)+1
  
###Finding the most prolific emailer
bigcount=None
bigword=None

for word,count in dicio.items():
 if bigcount is None or count>bigcount:
  bigword=word
  bigcount=count

print bigword,bigcount
hand.close()


 
 

