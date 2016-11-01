import re

##creating a handle and reading the text into a string

texto=open('regex_sum_209839.txt').read()

#creating a list where the numbers on the text are represented as strings
lista=re.findall('[0-9]+',texto)

##converting the strings into integers and adding the elements of the list
soma=sum([int(it) for it in lista])

print soma

