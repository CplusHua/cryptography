###
###    Date:2018-07-30
###   Time:03:33 GMT
###  Author:nianhua
###

之前主要写的是那enbase32和debase32这两个文件，现在觉得不是很方便</br>所以就写在一起了，介绍一下怎么使用
````
└──╼ #ipython3
Python 3.6.6 (default, Aug 07 2018, 03:44:17) 
Type "copyright", "credits" or "license" for more information.

In [1]: from NHbase32 import *

In [2]: newobj = base32("abcdefghijklmnop!@#$%^&1234567890")

In [3]: print(newobj.enbase32("nianhua"))
n3%&c5$io^!!====

In [4]: print(newobj.debase32(newobj.enbase32("nianhua")))
nianhua

````
最关键的地方在于初始化对象的时候可以选择性的是否传入一个新的字母表用来加密解密。</br>
如果你有什么特殊的需求，你就可以在这里修改为自己想用的字母表。


````
File enbase32.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
  annotation:The main purpose is to solve the malformed base encryption

File debase32.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
  annotation:The main purpose is to solve the malformed base encryption

---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------

└──╼ $python3 enbase32.py 
请输入要转换的字符串:abcdefghijk
MFRGGZDFMZTWQ2LKNM======

---------------------------------------------------------------------------------

└──╼ $python3 debase32.py 
请输入base32加密后的数据:MFRGGZDFMZTWQ2LKNM======
abcdefghijk

Some places to pay attention to：
  alphabet is variable, But it needs to be consistent. 
````




