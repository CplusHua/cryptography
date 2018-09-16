from numpy import *
#为什么说这是个失败的程序，是因为我居然想着自己去实现往里输入矩阵，我的天啊，我是不是傻～～


def JudgeIntNum(floatNum):

	floatNum = len(floatNum)**0.5

	if floatNum == 1:

		return 1

	intNum = int(floatNum)

	difVar = floatNum - intNum

	if difVar == 0 :

		return floatNum

	else:

		return 1




plaintext = input("please input plaintext (eg:example):")

password = input("please input password (eg:5,17,4,15):")

encryMatrix = []

password = password.split(',')

rank = int(JudgeIntNum(password))

if rank == 1:

	print("加密矩阵不符合要求！")
	exit()

for i in range(rank):

	matrixTmp = []

	for j in range(rank):

		matrixTmp.append(password[i*rank+j])

	encryMatrix.append(matrixTmp)

print(password)

print(encryMatrix)
