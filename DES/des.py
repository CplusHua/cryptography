# -*- coding: utf-8 -*-
import base64

hexadecimalcontrast = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]
S = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13, ],
     [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9, ],
     [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12, ],
     [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14, ],
     [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3, ],
     [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13, ],
     [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12, ],
     [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11, ]]
PC_1 = [57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4, ]
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32, ]
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25, ]
movnum = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def HexToBin(string):
    "Convert sixteen to binary"

    Binstring = ""
    string = string.lower()
    for i in string:
        try:
            Binstring += hexadecimalcontrast[i]
        except:
            return -1
    return Binstring


def BinToStr(strbin):
    "Turn the binary string to a ASCII string"

    strten = ""
    for i in range(len(strbin) // 8):
        num = 0
        test = strbin[i * 8:i * 8 + 8]
        for j in range(8):
            num += int(test[j]) * (2**(7 - j))
        strten += chr(num)
    return strten


def StrToHex(string):
    "Converts a string to HEX"

    hexStr = ''
    for i in string:
        tmp = str(hex(ord(i)))
        if len(tmp) == 3:
            hexStr += tmp.replace('0x', '0')
        else:
            hexStr += tmp.replace('0x', '')
    return hexStr


def Binxor(string1, string2):
    "If the length is different, only the short one is returned."

    strlen = 0
    xorstr = ""
    if len(string1) > len(string2):
        strlen = len(string2)
    else:
        strlen = len(string1)
    for i in range(strlen):
        if string1[i] == string2[i]:
            xorstr += '0'
        else:
            xorstr += '1'
    return xorstr

# 上面这四个函数没啥用


def SubstitutionBox(keyfield, sub):  # 置换盒

    newkeyfield = ''

    for i in range(len(sub)):

        newkeyfield += keyfield[sub[i] - 1]  # watch the table

    return newkeyfield


def SubkeyGeneration(freq, C, D):  # 轮密钥生成函数

    for i in range(movnum[freq]):

        C = C[1:] + C[:1]
        D = D[1:] + D[:1]

    return C, D, SubstitutionBox(C + D, PC_2)


def enkey(secretkey):  # 生成子密钥

    netss = SubstitutionBox(HexToBin(StrToHex(secretkey)), PC_1)

    C, D = netss[:28], netss[28:]

    key = []

    for i in range(16):  # 十六轮子密钥生成

        C, D, keyone = SubkeyGeneration(i, C, D)

        key.append(keyone)

    return key


def Sbox(plaintext, sub):

    # 压缩替换呀
    return HexToBin("%x" % S[sub][int(plaintext[:1] + plaintext[-1:], 2) * 16 + int(plaintext[1:-1], 2)])


def Function(plaintext, secretkey):
    "F函数，唯一的非线性环节依靠S盒实现"

    plaintext = Binxor(SubstitutionBox(plaintext, E),
                       secretkey)  # 经过E盒扩充异或当前key 48bit

    sout = ''

    for i in range(8):

        sout += Sbox(plaintext[i * 6:(i + 1) * 6], i)  # S盒，唯一的非线性结构

    sout = SubstitutionBox(sout, P)  # 使用P盒置换

    return sout


def endecrypt(plaintext, secretkey):
    "加解密函数，通过传入密文/明文,keys[]是一个数组进行解密或加密"

    netss = SubstitutionBox(HexToBin(StrToHex(plaintext)), IP)  # 使用IP盒置换

    L, R = netss[:32], netss[32:]  # 左右分块

    for i in range(16):  # Feistel怎么可以这么简洁

        L, R = R, Binxor(L, Function(R, secretkey[i]))  # 使用F函数加密R和KEY

    return SubstitutionBox(R + L, IP_1)  # 返回IP-1置换的结果


def encryption(plaintext, secretkey):

    # 这里是有问题的，如果当前长度正好等于8呢，会多余的添加8个00字符
    plaintext = plaintext + (8 - len(plaintext) % 8) * '\0'

    keys = enkey(secretkey[:8])  # 生成轮密钥16个

    ciphertext = ''

    for i in range(len(plaintext) / 8):

        # 每8位分块进行加密
        ciphertext += endecrypt(plaintext[i * 8:(i + 1) * 8], keys)

    # 输出模式可以在这里修改：StrToHex(BinToStr(ciphertext))
    return base64.b64encode(BinToStr(ciphertext))


def decryption(ciphertext, secretkey):

    ciphertext = base64.b64decode(ciphertext)

    keys = enkey(secretkey[:8])[::-1]  # 生成轮密钥，不过这个是逆序的

    plaintext = ''

    for i in range(len(ciphertext) / 8):

        plaintext += endecrypt(ciphertext[i * 8:(i + 1) * 8], keys)  # 分块进行解密

    return BinToStr(plaintext)


print decryption(encryption("happy every day,thank you very much", 'BobAlicezxx'), 'BobAlicezxx')
