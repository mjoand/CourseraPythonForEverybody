###Week 2 Exercise using list comprehension

import re

print sum([int(it) for it in re.findall('[0-9]+',open('regex_sum_209839.txt').read())])