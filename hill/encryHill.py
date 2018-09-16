from numpy import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'

plaintext = input("输入你想加密的内容(例如:example):")

encryMatrix = input("输入一个加密矩阵(例如:5,17;4,15):")

maxNum = len(encryMatrix.split(';'))

encryMatrix = mat(encryMatrix)

rank = linalg.matrix_rank(encryMatrix)

if rank != maxNum or rank == 1:

	print("输入的矩阵不符合要求!")

	exit()

if len(plaintext)%rank:

	plaintext += 'x' * (rank - len(plaintext)%rank)

numPlain = []

for i in range(rank):

	tmpNumPlain = []

	for j in range(len(plaintext)//rank):

		tmpNumPlain.append(alphabet.find(plaintext[j*rank+i])+1)

	numPlain.append(tmpNumPlain)

numPlain = mat(numPlain)

cipherMatrix = transpose(dot(encryMatrix,numPlain)).getA()

for i  in cipherMatrix:

	for j in i:

		print (alphabet[j%26-1],end='')


print()
