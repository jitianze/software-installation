#!/usr/bin/env python
# --coding:utf-8--

import string
import random

f = open("jihuoma.txt",'wb')
for i in range(200):
	chars = string.letters + string.digits
	s = [random.choice(chars)for i in range(8)]
	f.write(''.join(s) + '\n')
f.close()

