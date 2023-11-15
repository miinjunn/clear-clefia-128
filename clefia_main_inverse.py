from fungsi import xor_, f0, f1
from clefia_key_scheduling import rk

# plaintext                00010203 04050607 08090a0b 0c0d0e0f
# key                      ffeeddcc bbaa9988 77665544 33221100
# L                        8f89a61b 9db9d0f3 93e65627 da0d027e
# ciphertext               de2bf2fd 9b74aacd f1298555 459494fd


# ----------------------------------------------------------------------------------------
cipher = [[222, 43, 242, 253], [155, 116, 170, 205],
          [241, 41, 133, 85], [69, 148, 148, 253]]
key = [[255, 238, 221, 204], [187, 170, 153, 136],
       [119, 102, 85, 68], [51, 34, 17, 0]]


def gFn4_inv_18(inp, key, rk):
    x0 = inp[0]
    x1 = xor_(inp[1], key[2])
    x2 = inp[2]
    x3 = xor_(inp[3], key[3])
    for i in range(18):

        x1 = xor_(x1, (f0(x0, rk[2*(18-i)-2])))

        x3 = xor_(x3, (f1(x2, rk[2*(18-i)-1])))

        temp = x3
        x3 = x2
        x2 = x1
        x1 = x0
        x0 = temp
    return x0, x1, x2, x3

# INVERSE:
# t0, t1, t2, t3 = gFn4_inv_18(inp=cipher, key=key, rk=rk)
# plain = t1 + xor_(t2, key[0]) + t3 + xor_(t0, key[1])
# print(plain)
# plain = [hex(i)[2:] for i in plain]
# print(plain)
# print(len(plain))


# DECRYPT:
def decypt(cipher, key):
    # generate plaintext
    t0, t1, t2, t3 = gFn4_inv_18(inp=cipher, key=key, rk=rk)
    plain = t1 + xor_(t2, key[0]) + t3 + xor_(t0, key[1])
    plain_hex = []
    for i in plain:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        plain_hex.append(cek)
    return plain_hex


dec = decypt(cipher=cipher, key=key)
print(f"plaintext \t: {dec}")
print(f"len plain \t: {len(dec)}")
for i in dec:
    print(i, end='')
