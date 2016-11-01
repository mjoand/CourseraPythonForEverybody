import re
hand=open('regex_sum_209839.txt')
lista=list()

for line in hand:
 lista=lista+re.findall('[0-9]+',line)
 
soma=0

for it in lista:
 soma=soma+int(it)
 
print soma

hand.close()