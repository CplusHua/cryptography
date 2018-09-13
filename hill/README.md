###
###    Date:2018-09-12
###   Time:11:50 GMT
###  Author:nianhua
###

hill密码是古典密码中多表代换密码中的一部分。</br>
````
原理：希尔密码(Hill Password)是运用基本矩阵论原理的替换密码，由Lester S. Hill在1929年发明。
每个字母当作26进制数字:A=0, B=1, C=2... 一串字母当成n维向量，跟一个n×n的矩阵相乘，再将得出的结果模26。
注意用作加密的矩阵(即密匙)在\mathbb_^n必须是可逆的，否则就不可能译码。只有矩阵的行列式和26互质，才是可逆的。
````
Invented by Lester S. Hill in 1929, the Hill cipher is a polygraphic substitution cipher based on linear algebra. Hill used matrices and matrix multiplication to mix up the plaintext.

To counter charges that his system was too complicated for day to day use, Hill constructed a cipher machine for his system using a series of geared wheels and chains. However, the machine never really sold.

Hill's major contribution was the use of mathematics to design and analyse cryptosystems. It is important to note that the analysis of this algorithm requires a branch of mathematics known as number theory. Many elementary number theory text books deal with the theory behind the Hill cipher, with several talking about the cipher in detail (e.g. Elementary Number Theory and its applications, Rosen, 2000). It is advisable to get access to a book such as this, and to try to learn a bit if you want to understand this algorithm in depth.

For a guide on how to break Hill ciphers, see Cryptanalysis of the Hill Cipher.

Example 
This example will rely on some linear algebra and some number theory. The key for a hill cipher is a matrix e.g.



In the above case, we have taken the size to be 3×3, however it can be any size (as long as it is square). Assume we want to encipher the message ATTACK AT DAWN. To encipher this, we need to break the message into chunks of 3. We now take the first 3 characters from our plaintext, ATT and create a vector that corresponds to the letters (replace A with 0, B with 1 ... Z with 25 etc.) to get: [0 19 19] (this is ['A' 'T' 'T']).

To get our ciphertext we perform a matrix multiplication (you may need to revise matrix multiplication if this doesn't make sense):



This process is performed for all 3 letter blocks in the plaintext. The plaintext may have to be padded with some extra letters to make sure that there is a whole number of blocks.

Now for the tricky part, the decryption. We need to find an inverse matrix modulo 26 to use as our 'decryption key'. i.e. we want something that will take 'PFO' back to 'ATT'. If our 3 by 3 key matrix is called K, our decryption key will be the 3 by 3 matrix K-1, which is the inverse of K.



To find K-1 we have to use a bit of maths. It turns out that K-1 above can be calculated from our key. A lengthy discussion will not be included here, but we will give a short example. The important things to know are inverses (mod m), determinants of matrices, and matrix adjugates.

Let K be the key matrix. Let d be the determinant of K. We wish to find K-1 (the inverse of K), such that K × K-1 = I (mod 26), where I is the identity matrix. The following formula tells us how to find K-1 given K:



where d × d-1 = 1(mod 26), and adj(K) is the adjugate matrix of K.

d (the determinant) is calculated normally for K (for the example above, it is 489 = 21 (mod 26)). The inverse, d-1, is found by finding a number such that d × d-1 = 1 (mod 26) (this is 5 for the example above since 5*21 = 105 = 1 (mod 26)). The simplest way of doing this is to loop through the numbers 1..25 and find the one such that the equation is satisfied. There is no solution (i.e. choose a different key) if gcd(d,26) ≠ 1 (this means d and 26 share factors, if this is the case K can not be inverted, this means the key you have chosen will not work, so choose another one).

That is it. Once K-1 is found, decryption can be performed.
