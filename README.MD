# RSA Algorithm (  Encryption - Decryption )

The following project contains [Python3](https://docs.python.org/3/) implementation of [RSA Algorithm (Encryption - Decryption)](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/).



## Explanation :

![description](https://user-images.githubusercontent.com/48678280/87449188-223c5b00-c5fd-11ea-8b21-b1afbbb12bc5.jpg)


```
1.  Take two big prime numbers p, q.
    Calculate the values of : 
        n = pq
        t = (p-1)(q-1)
2.  Calculate Encryption Key :
        e -> gcd(e,z)==1;      1 < e < z
3.  Calculate Decryption Key :
        d -> ed = 1(mod z);    1 <d < z
4.  Get the Encrypted/Cypher text(C) and Decrypted/Plain text(P) :
        C = (P ^ e) % n
        P = (C ^ d) % n
```





> سبحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لا إِلهَ إِلأَ انْتَ أَسْتَغْفِرُكَ وَأَتْوبُ إِلَيْكَ.
