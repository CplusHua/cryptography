#密文:mttpjbpexfdzcegtdzeanutg
#密钥:[[3,1],[2,1]]

from numpy import *

alphatext = 'abcdefghijklmnopqrstuvwxyz'

key = array([[3,1],[2,1]])

miwen = array([[12,19,9,15,23,3,2,6,3,4,13,19],[19,15,1,4,5,25,4,19,25,0,20,6]])

print miwen

key_1 = linalg.inv(key)

print key_1

test = dot(key_1,miwen)

print test

for i in test:
	for j in i:

		print alphatext[int(round(j))%26],

	print ''
