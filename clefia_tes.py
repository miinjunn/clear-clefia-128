from fungsi import S0, S1, M0, M1, m0_mix, m1_mix

# Diffusion Matrices
# y = M0 trans(T) adalah


# def M0_trans(T0, T1, T2, T3):
#     y0 = T0 ^ (0x02 * T1) ^ (0X04 * T2) ^ (0X06 * T3)
#     y1 = (0X02 * T0) ^ (T1) ^ (0X06 * T2) ^ (0X04 * T3)
#     y2 = (0X04 * T0) ^ (0X06 * T1) ^ (T2) ^ (0X02 * T3)
#     y3 = (0X06 * T0) ^ (0X04 * T1) ^ (0X02 * T2) ^ (T3)
#     return y0, y1, y2, y3

# y = M1 trans(T) adalah


# def M1_trans(T0, T1, T2, T3):
#     y0 = T0 ^ (0x08 * T1) ^ (0x02 * T2) ^ (0x0a * T3)
#     y1 = (0x08 * T0) ^ T1 ^ (0x0a * T2) ^ (0x02 * T3)
#     y2 = (0x02 * T0) ^ (0x0a * T1) ^ T2 ^ (0x08 * T3)
#     y3 = (0x0a * T0) ^ (0x02 * T1) ^ (0x08 * T2) ^ T3
#     return y0, y1, y2, y3


# input     : 32-bit round key RK, 32-bit data x,
# output    : 32-bit data y

# def F0(rk, x):
#     T = rk ^ x
#     T0 = S0[T0]
#     T1 = S1[T1]
#     T2 = S0[T2]
#     T3 = S1[T3]
#     # T = T0 + T1 + T2 + T3
#     y0, y1, y2, y3 = M0_trans(T0, T1, T2, T3)
#     y = y0 + y1 + y2 + y3
#     return y


# def F1(rk, x):
#     T = rk ^ x
#     T0 = S1[T0]
#     T1 = S0[T1]
#     T2 = S1[T2]
#     T3 = S0[T3]
#     # T = T0 + T1 + T2 + T3
#     y0, y1, y2, y3 = M1_trans(T0, T1, T2, T3)
#     y = y0 + y1 + y2 + y3
#     return y


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
