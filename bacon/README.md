###
###    Date:2018-08-06
###   Time:12:33 GMT
###  Author:nianhua
###

````
  培根密码，又名倍康尼密码（英语：Bacon's cipher）是由法兰西斯·培根发明的一种隐写术。
  明文中的每个字母都会转换成一组五个英文字母。其转换依靠下表：
  a	AAAAA	  g	AABBA	  n	ABBAA	  t	BAABA
  b	AAAAB	  h	AABBB	  o	ABBAB	  u-v	BAABB
  c	AAABA	  i-j	ABAAA	p	ABBBA	  w	BABAA
  d	AAABB	  k	ABAAB	  q	ABBBB	  x	BABAB
  e	AABAA	  l	ABABA	  r	BAAAA	  y	BABBA
  f	AABAB	  m	ABABB	  s	BAAAB	  z	BABBB
  
  培根密码实际上就是一种替换密码，根据所给表一一对应转换即可加密解密 。它的特殊之处在于：
可以通过不明显的特征来隐藏密码信息，比如大小写、正斜体等，只要两个不同的属性，密码即可隐藏。
  
  举例：
bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE
 直接放入CapitalDeBacon.py
---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------
此程序只使用了密文对照表中的第二张表，且AB的顺序请自行斟酌
输入要解密的密文:bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE
AAAABAAAAAAAABAABBABABBAAABAAABAAABABBAAABBABBAABAAABABABBABABBABAAABB
baconisnotfood
---------------------------------------------------------------------------------
end
---------------------------------------------------------------------------------            
````
