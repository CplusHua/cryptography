###
###    Date:2018-07-31
###   Time:14:47 GMT
###  Author:nianhua
###
更新：NHbase64.py</br>
这次把加密和解密封装到一个类里了，如果要用的话直接使用即可</br>
举例：
````
└──╼ $ipython3 
Python 3.6.6 (default, Aug 7 2018, 14:44:17) 
Type "copyright", "credits" or "license" for more information.

In [1]: from NHbase64 import *

In [2]: newobj = base64("qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP-|0987654321")

In [3]: print(newobj.enbase64("nianhua"))
ATVDATD|lh==

In [4]: print(newobj.debase64("ATVDATD|lh=="))
nianhua
````

我觉得最有用的还是可以自定义字母表，再想想有什么办法可以base任意就好了，研究一下吧</br>
还有一个比较明显的特征是，要识别base加密可以看某些字符加密后是否含有==

````
File enbase64.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  annotation:The main purpose is to solve the malformed base encryption

File debase64.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  annotation:The main purpose is to solve the malformed base encryption

---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------

└──╼ $python3 enbase64.py
请输入要转换的字符串:nian-hua  
bmlhbi1odWE=

---------------------------------------------------------------------------------

└──╼ $python3 debase64.py 
请输入base64加密后的数据:bmlhbi1odWE=
nian-hua

Some places to pay attention to：
  alphabet is variable, But it needs to be consistent. 
  Although there are many base64/base32 programs, this program can set the alphabet by itself.
  I think this is the best place.
````




