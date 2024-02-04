# RSA Algorithm Implementation in Python

## Overview
This project implements the RSA (Rivest–Shamir–Adleman) algorithm, a popular asymmetric encryption and decryption method, using Python. RSA is widely used for secure data transmission in modern computing. The implementation allows users to encrypt and decrypt text using RSA, providing insights into the algorithm's mechanics.

## Features
- RSA algorithm for encryption and decryption
- Reading plaintext from a file or input
- Prime number validation for keys
- ASCII conversion for text encryption and decryption

## Prerequisites
- Python 3.x
- `sympy` library for prime number validation

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbdelrahmanBayoumi/RSA-Algorithm-in-Cryptography.git
   ```
2. Install the required Python library:
   ```bash
   pip install sympy
   ```

## Usage
To use this program:
1. Run `main.py`.
2. Input two prime numbers (p and q) when prompted.
3. Choose to read from a file (`f`) or input plaintext (`m`).
4. The program will display the encrypted and decrypted message.

### Example
```bash
Enter p: 17
Enter q: 19
Enter:-
    - 'f' to read from file => msg.txt.
    - 'm' to enter plaintext message.
f
```

## Algorithm Explanation

![description](https://user-images.githubusercontent.com/48678280/87449188-223c5b00-c5fd-11ea-8b21-b1afbbb12bc5.jpg)

RSA algorithm involves the following steps:
1. Select two large prime numbers `p` and `q`. Calculate `n = p * q` and `t = (p - 1) * (q - 1)`.
2. Choose an encryption key `e` such that `1 < e < t` and `gcd(e, t) == 1`.
3. Determine the decryption key `d` satisfying `d * e = 1 (mod t)`.
4. For encryption, convert plaintext to ASCII and compute `C = (P ^ e) % n`.
5. For decryption, convert cipher text back using `P = (C ^ d) % n`.

## Contributing
Contributions to this project are welcome. Please follow standard GitHub contribution guidelines.

## Acknowledgements
Developed by Abdelrahman Bayoumi - [GitHub](https://github.com/AbdelrahmanBayoumi). Course project for Algorithm Analysis and Design CS305, Faculty of Science, Alexandria University.


<h6 align=center>سبحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لا إِلهَ إِلأَ انْتَ أَسْتَغْفِرُكَ وَأَتْوبُ إِلَيْكَ.</h6>
