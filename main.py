"""
RSA Algorithm in Cryptography
This program is Implemented by Abdelrahman Bayoumi - https://github.com/AbdelrahmanBayoumi
Algorithm Analysis and Design CS305 - Faculty Of Science, Alexandria University
"""

import math
import sympy


def read_file(file_path):
    return open(file_path).read()


def isINT(num):
    if num % 1 == 0:
        return True
    return False


def isPrime(n):
    return sympy.isprime(n)


def calc_e(t):
    for e in range(2, t):
        if math.gcd(e, t) == 1:
            return e
    return None


def calc_d(t, e):
    d = 0
    L = 0
    while True:
        d = (t * L + 1) / e
        if isINT(d):
            break
        L += 1
    return int(d)


def encrypt(public_key, message):
    e, n = public_key
    # pow(with three arguments) => x**y % z
    return pow(message, e, n)


def encrypt_string(public_key, input_string):
    list_ascii_p = format_message(input_string)
    print("list_ascii_numbers(BEFORE ENCRYPTION) : ", list_ascii_p)
    list_cipher_ascii = []
    for i in list_ascii_p:
        list_cipher_ascii.append(encrypt(public_key, i))
    print("list_ascii_numbers(AFTER ENCRYPTION) : ", list_cipher_ascii)
    return list_cipher_ascii


def decrypt(private_key, cipher_text):
    d, n = private_key
    # pow(with three arguments) => x**y % z
    p = pow(cipher_text, d, n)
    return p


def decrypt_string(private_key, list_cipher_ascii):
    list_decrypted_ascii = []
    for i in list_cipher_ascii:
        list_decrypted_ascii.append(decrypt(private_key, i))
    return list_decrypted_ascii


def format_message(input_string):
    list_ascii = []
    for i in range(len(input_string)):
        list_ascii.append(ord(input_string[i]))
    return list_ascii


def covert_ascii_to_char(list_items):
    char_list = ""
    for i in range(len(list_items)):
        char_list += (chr(list_items[i] % 0x10ffff))
    return char_list


def RSA(p, q, plain_text=""):
    n = p * q
    t = (p - 1) * (q - 1)
    e = calc_e(t)
    d = calc_d(t, e)
    publicKey = (e, n)
    print("Public Key ( e= ", e, ", n= ", n, ")")
    privateKey = (d, n)
    print("Private Key ( d= ", d, ", n= ", n, ")")
    if plain_text == "":
        plain_message = read_file('msg.txt')
    else:
        plain_message = plain_text
    print("Encrypting (", plain_message, ") ...")
    cipher_message = encrypt_string(publicKey, plain_message)
    print("Decrypting (", cipher_message, ") ...")
    p = decrypt_string(privateKey, cipher_message)
    print("plain_message(ASCII) : ", p)
    print("plain_message(CHAR) : ", covert_ascii_to_char(p))
    return cipher_message, p


def main():
    p = int(input("Enter p : "))
    if not isPrime(p):
        raise ValueError("P is not prime")
    q = int(input("Enter q : "))
    if not isPrime(q):
        raise ValueError("q is not prime")
    flag = input("Enter:-\n\t- 'f' to read from file => msg.txt.\n\t- 'm' to enter plaintext message.\n")
    if flag == 'f':
        return RSA(p, q)
    elif flag == 'm':
        m = input("Enter plaintext message:")
        return RSA(p, q, m)
    else:
        print("Error !")
        return None


if __name__ == '__main__':
    Cypher, Plain = main()
    # print("Encrypted (Cypher text) : ", c)
    # print("Decrypted (Plain text) : ", p)


