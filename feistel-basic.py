# 1 input 8 character
# 2 split into 2 part (4 character each)
# 3 like this:
#  Left(L0)               Right(R0)
#  32 bits                32 bits
# 4 encode R0 using F function -> Fs(R0) -> hasil: E
# 5
# L1 = R0
# R1 = E xor L0
# 6 concate L1 + R1


while True:
    plaintext = input("input plaintext: ")
    key_feistel = input("input key: ")
    tes: str = "loading"
    print(f"{tes:.^19}")

    plaintext = [i.encode(encoding="ascii").hex() for i in plaintext]

    if len(plaintext) > 8:
        print(f"> len text: {len(plaintext)}")
        print("> input reach max limit (8 char)")

    elif len(plaintext) < 8:
        for i in range(8):
            if len(plaintext) < 8:
                plaintext.append("00")
        break

    elif len(plaintext) == 8:
        break

# plaintext = [i for i in plaintext]
# print(plaintext)

plaintext = [int(i, base=16) for i in plaintext]

print(plaintext)
print(len(plaintext))


def split(plain: list):
    temp = [i for i in plain[:len(plain)//2]]
    temp2 = [i for i in plain[len(plain)//2:]]
    return temp, temp2


L0, R0 = split(plaintext)
print(f"L0: {L0}")
print(f"R0: {R0}")


def f_func(state: list):
    temp = []
    for i in state:
        temp.append(i // 2)
    return temp


f = f_func(R0)
print(f"r0 f_function: {f}")


def swap(L, R):
    L_new = R0
    r_new = []
    for i in range(4):
        temp = f[i] ^ L0[i]
        r_new.append(temp)
    return L_new, r_new


L1, R1 = swap(L0, R0)

print(f"L1: {L1}")
print(f"R1: {R1}")

print(f"gabungan: {L1 + R1}")
