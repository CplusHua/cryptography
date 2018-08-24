
alphabetb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"

ciphertext = input("请输入要破解的密码:")

for i in range(1,26):

    plaintext =""

    for j in ciphertext:
        
        if 64 < ord(j) < 91:
        
            plaintext += alphabetb[alphabetb.find(j)-i-1]
        
        elif 96 < ord(j) <123:

            plaintext += alphabets[alphabets.find(j)-i-1]

        else:

            plaintext += j
    
    print("%2d:%s"%(i,plaintext))
