from fungsi import S0, S1, M0, M1, m0_mix, m1_mix
from clefia_key_scheduling import rk, con_128

# ------------------------------------------------------------------------------------------
# x pada F0 dan F1 berukuran 32bit
# misal:
# x  = 0x00010203
# rk = 0xf3e6cef9
T0 = [0, 1, 2, 3]
rk0 = [243, 230, 206, 249]

# maka fungsi F1 pada round-0 adalah:


def f0(T0, rk):
    # (after key add)
    T = [(rk[i] ^ T0[i]) for i in range(4)]
    # hex
    # T_hex = [hex(i)[2:] for i in T]

    # sub-S1 untuk T (after S)
    T[0] = S0[T[0]]
    T[1] = S1[T[1]]
    T[2] = S0[T[2]]
    T[3] = S1[T[3]]
    # hex
    # T_hex = [hex(i)[2:] for i in T]

    # (after M)
    Y = [T[0], T[1], T[2], T[3]]
    f0_output = m0_mix(Y)
    # print(f"F1 output round-1: {f1_output}")

    # hex
    # f1_output = [hex(i)[2:] for i in f1_output]
    return f0_output


lane1 = f0(T0, rk0)
print(f"f0 after M (round-0): {lane1}")
lane1_hex = [hex(i)[2:] for i in lane1]
print(f"f0_hex after M (round-0): {lane1_hex}")


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# x pada F0 dan F1 berukuran 32bit
# misal:
# x  = 0x08090a0b
# rk = 0x8df75e38
T2 = [8, 9, 10, 11]
rk1 = [141, 247, 94, 56]

# maka fungsi F1 pada round-0 adalah:


def f1(T2, rk):
    # (after key add)
    T = [(rk[i] ^ T2[i]) for i in range(4)]
    # hex
    # T_hex = [hex(i)[2:] for i in T]

    # sub-S1 untuk T (after S)
    T[0] = S1[T[0]]
    T[1] = S0[T[1]]
    T[2] = S1[T[2]]
    T[3] = S0[T[3]]
    # hex
    # T_hex = [hex(i)[2:] for i in T]

    # (after M)
    Y = [T[0], T[1], T[2], T[3]]
    f1_output = m1_mix(Y)
    # print(f"F1 output round-1: {f1_output}")

    # hex
    # f1_output = [hex(i)[2:] for i in f1_output]
    return f1_output


lane3 = f1(T2, rk1)
print(f"f1 after M (round-0): {lane3}")
lane3_hex = [hex(i)[2:] for i in lane3]
print(f"f1_hex after M (round-0): {lane3_hex}")

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

plaintext = [0x00, 0x01, 0x02, 0x03,
             0x04, 0x05, 0x06, 0x07,
             0x08, 0x09, 0x0a, 0x0b,
             0x0c, 0x0d, 0x0e, 0x0f]

plaintext = [int(hex(i)[2:], base=16) for i in plaintext]

plain = []
for i in range(4):
    plain.append(plaintext[i*4:i*4+4])

print(plain)
# ----------------------------------------------------------------------------------------
keytext = [0xff, 0xee, 0xdd, 0xcc,
           0xbb, 0xaa, 0x99, 0x88,
           0x77, 0x66, 0x55, 0x44,
           0x33, 0x22, 0x11, 0x00]

key = [int(hex(i)[2:], base=16) for i in keytext]
# print(key)

wk = []
for i in range(4):
    wk.append(key[i*4:i*4+4])

print(wk)
# ----------------------------------------------------------------------------------------


def xor_(state1, state2):
    temp = []
    for i in range(len(state1)):
        temp.append(state1[i] ^ state2[i])
    return temp


def gFn4_18(inp0, inp1, inp2, inp3):
    x0 = inp0
    x1 = xor_(inp1, wk[0])
    x2 = inp2
    x3 = xor_(inp3, wk[1])
    for i in range(18):

        x1 = xor_(x1, (f0(x0, rk[2*i])))

        x3 = xor_(x3, (f1(x2, rk[2*i+1])))

        temp = x0
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = temp
    return x0, x1, x2, x3


c0, c1, c2, c3 = gFn4_18(plain[0], plain[1], plain[2], plain[3])

# cipher = c0 + (xor_(c1, wk[2])) + c2 + (xor_(c3, wk[3]))
cipher = c3 + (xor_(c0, wk[2])) + c1 + (xor_(c2, wk[3]))

cipher_hex = [hex(i)[2:] for i in cipher]
print(f"cipher_hex: {cipher_hex}")
