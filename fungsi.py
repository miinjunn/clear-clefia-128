# import galois

# S-Box untuk F0
S0 = [0x57, 0x49, 0xd1, 0xc6, 0x2f, 0x33, 0x74, 0xfb,
      0x95, 0x6d, 0x82, 0xea, 0x0e, 0xb0, 0xa8, 0x1c,
      0x28, 0xd0, 0x4b, 0x92, 0x5c, 0xee, 0x85, 0xb1,
      0xc4, 0x0a, 0x76, 0x3d, 0x63, 0xf9, 0x17, 0xaf,
      0xbf, 0xa1, 0x19, 0x65, 0xf7, 0x7a, 0x32, 0x20,
      0x06, 0xce, 0xe4, 0x83, 0x9d, 0x5b, 0x4c, 0xd8,
      0x42, 0x5d, 0x2e, 0xe8, 0xd4, 0x9b, 0x0f, 0x13,
      0x3c, 0x89, 0x67, 0xc0, 0x71, 0xaa, 0xb6, 0xf5,
      0xa4, 0xbe, 0xfd, 0x8c, 0x12, 0x00, 0x97, 0xda,
      0x78, 0xe1, 0xcf, 0x6b, 0x39, 0x43, 0x55, 0x26,
      0x30, 0x98, 0xcc, 0xdd, 0xeb, 0x54, 0xb3, 0x8f,
      0x4e, 0x16, 0xfa, 0x22, 0xa5, 0x77, 0x09, 0x61,
      0xd6, 0x2a, 0x53, 0x37, 0x45, 0xc1, 0x6c, 0xae,
      0xef, 0x70, 0x08, 0x99, 0x8b, 0x1d, 0xf2, 0xb4,
      0xe9, 0xc7, 0x9f, 0x4a, 0x31, 0x25, 0xfe, 0x7c,
      0xd3, 0xa2, 0xbd, 0x56, 0x14, 0x88, 0x60, 0x0b,
      0xcd, 0xe2, 0x34, 0x50, 0x9e, 0xdc, 0x11, 0x05,
      0x2b, 0xb7, 0xa9, 0x48, 0xff, 0x66, 0x8a, 0x73,
      0x03, 0x75, 0x86, 0xf1, 0x6a, 0xa7, 0x40, 0xc2,
      0xb9, 0x2c, 0xdb, 0x1f, 0x58, 0x94, 0x3e, 0xed,
      0xfc, 0x1b, 0xa0, 0x04, 0xb8, 0x8d, 0xe6, 0x59,
      0x62, 0x93, 0x35, 0x7e, 0xca, 0x21, 0xdf, 0x47,
      0x15, 0xf3, 0xba, 0x7f, 0xa6, 0x69, 0xc8, 0x4d,
      0x87, 0x3b, 0x9c, 0x01, 0xe0, 0xde, 0x24, 0x52,
      0x7b, 0x0c, 0x68, 0x1e, 0x80, 0xb2, 0x5a, 0xe7,
      0xad, 0xd5, 0x23, 0xf4, 0x46, 0x3f, 0x91, 0xc9,
      0x6e, 0x84, 0x72, 0xbb, 0x0d, 0x18, 0xd9, 0x96,
      0xf0, 0x5f, 0x41, 0xac, 0x27, 0xc5, 0xe3, 0x3a,
      0x81, 0x6f, 0x07, 0xa3, 0x79, 0xf6, 0x2d, 0x38,
      0x1a, 0x44, 0x5e, 0xb5, 0xd2, 0xec, 0xcb, 0x90,
      0x9a, 0x36, 0xe5, 0x29, 0xc3, 0x4f, 0xab, 0x64,
      0x51, 0xf8, 0x10, 0xd7, 0xbc, 0x02, 0x7d, 0x8e]

# S-Box untuk F1
S1 = [0x6c, 0xda, 0xc3, 0xe9, 0x4e, 0x9d, 0x0a, 0x3d,
      0xb8, 0x36, 0xb4, 0x38, 0x13, 0x34, 0x0c, 0xd9,
      0xbf, 0x74, 0x94, 0x8f, 0xb7, 0x9c, 0xe5, 0xdc,
      0x9e, 0x07, 0x49, 0x4f, 0x98, 0x2c, 0xb0, 0x93,
      0x12, 0xeb, 0xcd, 0xb3, 0x92, 0xe7, 0x41, 0x60,
      0xe3, 0x21, 0x27, 0x3b, 0xe6, 0x19, 0xd2, 0x0e,
      0x91, 0x11, 0xc7, 0x3f, 0x2a, 0x8e, 0xa1, 0xbc,
      0x2b, 0xc8, 0xc5, 0x0f, 0x5b, 0xf3, 0x87, 0x8b,
      0xfb, 0xf5, 0xde, 0x20, 0xc6, 0xa7, 0x84, 0xce,
      0xd8, 0x65, 0x51, 0xc9, 0xa4, 0xef, 0x43, 0x53,
      0x25, 0x5d, 0x9b, 0x31, 0xe8, 0x3e, 0x0d, 0xd7,
      0x80, 0xff, 0x69, 0x8a, 0xba, 0x0b, 0x73, 0x5c,
      0x6e, 0x54, 0x15, 0x62, 0xf6, 0x35, 0x30, 0x52,
      0xa3, 0x16, 0xd3, 0x28, 0x32, 0xfa, 0xaa, 0x5e,
      0xcf, 0xea, 0xed, 0x78, 0x33, 0x58, 0x09, 0x7b,
      0x63, 0xc0, 0xc1, 0x46, 0x1e, 0xdf, 0xa9, 0x99,
      0x55, 0x04, 0xc4, 0x86, 0x39, 0x77, 0x82, 0xec,
      0x40, 0x18, 0x90, 0x97, 0x59, 0xdd, 0x83, 0x1f,
      0x9a, 0x37, 0x06, 0x24, 0x64, 0x7c, 0xa5, 0x56,
      0x48, 0x08, 0x85, 0xd0, 0x61, 0x26, 0xca, 0x6f,
      0x7e, 0x6a, 0xb6, 0x71, 0xa0, 0x70, 0x05, 0xd1,
      0x45, 0x8c, 0x23, 0x1c, 0xf0, 0xee, 0x89, 0xad,
      0x7a, 0x4b, 0xc2, 0x2f, 0xdb, 0x5a, 0x4d, 0x76,
      0x67, 0x17, 0x2d, 0xf4, 0xcb, 0xb1, 0x4a, 0xa8,
      0xb5, 0x22, 0x47, 0x3a, 0xd5, 0x10, 0x4c, 0x72,
      0xcc, 0x00, 0xf9, 0xe0, 0xfd, 0xe2, 0xfe, 0xae,
      0xf8, 0x5f, 0xab, 0xf1, 0x1b, 0x42, 0x81, 0xd6,
      0xbe, 0x44, 0x29, 0xa6, 0x57, 0xb9, 0xaf, 0xf2,
      0xd4, 0x75, 0x66, 0xbb, 0x68, 0x9f, 0x50, 0x02,
      0x01, 0x3c, 0x7f, 0x8d, 0x1a, 0x88, 0xbd, 0xac,
      0xf7, 0xe4, 0x79, 0x96, 0xa2, 0xfc, 0x6d, 0xb2,
      0x6b, 0x03, 0xe1, 0x2e, 0x7d, 0x14, 0x95, 0x1d]


# Diffusion Matrices
# M0 untuk F0
M0 = [0x01, 0x02, 0x04, 0x06,
      0x02, 0x01, 0x06, 0x04,
      0x04, 0x06, 0x01, 0x02,
      0x06, 0x04, 0x02, 0x01]

# M0 untuk F1
M1 = [0x01, 0x08, 0x02, 0x0a,
      0x08, 0x01, 0x0a, 0x02,
      0x02, 0x0a, 0x01, 0x08,
      0x0a, 0x02, 0x08, 0x01]

# Constant Value
con128 = [0xf56b7aeb, 0x994a8a42, 0x96a4bd75, 0xfa854521,
          0x735b768a, 0x1f7abac4, 0xd5bc3b45, 0xb99d5d62,
          0x52d73592, 0x3ef636e5, 0xc57a1ac9, 0xa95b9b72,
          0x5ab42554, 0x369555ed, 0x1553ba9a, 0x7972b2a2,
          0xe6b85d4d, 0x8a995951, 0x4b550696, 0x2774b4fc,
          0xc9bb034b, 0xa59a5a7e, 0x88cc81a5, 0xe4ed2d3f,
          0x7c6f68e2, 0x104e8ecb, 0xd2263471, 0xbe07c765,
          0x511a3208, 0x3d3bfbe6, 0x1084b134, 0x7ca565a7,
          0x304bf0aa, 0x5c6aaa87, 0xf4347855, 0x9815d543,
          0x4213141a, 0x2e32f2f5, 0xcd180a0d, 0xa139f97a,
          0x5e852d36, 0x32a464e9, 0xc353169b, 0xaf72b274,
          0x8db88b4d, 0xe199593a, 0x7ed56d96, 0x12f434c9,
          0xd37b36cb, 0xbf5a9a64, 0x85ac9b65, 0xe98d4d32,
          0x7adf6582, 0x16fe3ecd, 0xd17e32c1, 0xbd5f9f66,
          0x50b63150, 0x3c9757e7, 0x1052b098, 0x7c73b3a7]


def break_input(inputan):
    temp = []
    input = [hex(ord(i))[2:] for i in inputan]      # convert ke hex
    while len(input) < 16:                          # padd 00 jika char < 16
        input.append("00")
    input = [int(i, base=16) for i in input]        # convert ke dec
    for i in range(4):                              # bagi menjadi 4 line
        temp.append(input[i*4:i*4+4])
    return temp


def redefine_con128(con128):
    temp = [hex(i)[2:] for i in con128]
    # temp = [i for i in temp]

    con_128 = []
    for i in temp:
        n = 2
        tiap_index = []
        for j in range(0, len(i), n):  # split tiap n karakter
            split_n = i[j:j+n]
            tiap_index.append(int(split_n, base=16))    # mengubah jadi decimal
        con_128.append(tiap_index)
    return con_128


# -------------------------------------------------------------------------------------------
# def gFn(state, pre_state):        # gfn irreducible -> untuk AES
#     p = 0
#     hiBitSet = 0
#     for i in range(8):
#         if pre_state & 1 == 1:
#             p ^= state
#         hiBitSet = state & 0x80
#         state <<= 1
#         if hiBitSet == 0x80:
#             state ^= 0x1b
#         pre_state >>= 1
#     return p % 256


# def gFn(a, b):          # gfn irreducible -> untuk AES
#     sum = 0
#     while (b > 0):
#         if (b & 1):
#             sum ^= a
#         b >>= 1
#         a <<= 1
#         if (a & 0x100):
#             a ^= 0x11B
#     return sum


# def gFn(state, prev_matrix):      # gfn primitive -> untuk CLEFIA (import galois)
#     GFN = galois.GF(2**8)
#     x = GFN(state)
#     y = GFN(prev_matrix)
#     return x * y

# -------------------------------------------------------------------------------------------

def gFn(state, pre_matrix):     # gfn primitive -> untuk CLEFIA
    p = 0
    while pre_matrix:
        if pre_matrix & 0b1:
            p ^= state
        state <<= 1
        if state & 0x100:
            state ^= 0b11101
        pre_matrix >>= 1
    return p & 0xff


# untuk M0
def m0_mix(state):
    hasil_GFN = []
    for i in range(4):
        hasil_GFN.append(gFn(state[0], M0[i*4]) ^ gFn(state[1], M0[i*4 + 1]) ^ gFn(
            state[2], M0[i*4 + 2]) ^ gFn(state[3], M0[i*4 + 3]))
    return hasil_GFN


# untuk M1
def m1_mix(state):
    hasil_GFN = []
    for i in range(4):
        hasil_GFN.append(gFn(state[0], M1[i*4]) ^ gFn(state[1], M1[i*4 + 1]) ^ gFn(
            state[2], M1[i*4 + 2]) ^ gFn(state[3], M1[i*4 + 3]))
    return hasil_GFN

# -------------------------------------------------------------------------------------------
# fungsi F0 dan F1


def f0(T0: list, rk: list):
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


def f1(T2: list, rk: list):
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


# -------------------------------------------------------------------------------------------
# fungsi transpose matrks
# matrix = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)]


def trans(matrik):
    trans_matrik = []
    # for row in matrik:                          # print matrix sebelum di-transpose
    #     print(row)
    # print("\n")
    # t_matrik = zip(*matrik)                   # return tuple
    t_matrik = map(list, zip(*matrik))          # return list
    for row in t_matrik:
        trans_matrik.append(row)
    return trans_matrik


# z = trans(matrix)

# -------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------
# Key Scheduling part:
# Generate L from K
def gFn4_12(wk, constant_value):
    x0 = wk[0]
    x1 = wk[1]
    x2 = wk[2]
    x3 = wk[3]
    for i in range(12):

        x1 = xor_(x1, (f0(x0, constant_value[2*i])))

        x3 = xor_(x3, (f1(x2, constant_value[2*i+1])))

        temp = x0
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = temp
    return x0, x1, x2, x3

# expand L and K to produce 36 Round Key
# Double Swap function:


def sigma(intermediate_key):
    split_bin = [bin(i)[2:] for i in intermediate_key]

    temp = ''
    for i in split_bin:
        for j in range(8):
            if len(i) < 8:
                i = '0' + i
        temp += i

    y0, y1, y2, y3 = temp[:7], temp[7:64], temp[64:121], temp[121:128]

    final = y1 + y3 + y0 + y2

    bin_pisah = []
    for i in range(16):
        bin_pisah.append(final[i*8:i*8+8])

    dec_pisah = [int(i, base=2) for i in bin_pisah]
    return dec_pisah


# generate RK function:
def generate_rk(key, L, constant_value):
    rk = []
    for i in range(9):
        T = xor_(L, (constant_value[4*i + 24] + constant_value[4*i +
                 25] + constant_value[4*i + 26] + constant_value[4*i + 27]))
        L = sigma(L)
        if i % 2 != 0:
            T = xor_(T, key)
        # print(f"RK{i}: {T}")
        # for k in range(len(T)):             # convert dec to hex
        #     T[k] = hex(T[k])[2:]
        # print(f"RK{i}: {T}")
        for j in range(4):
            rk.append(T[j*4: j*4+4])
    return rk


# -------------------------------------------------------------------------------------------
# encrypt:
def xor_(state1, state2):
    temp = []
    for i in range(len(state1)):
        temp.append(state1[i] ^ state2[i])
    return temp


def gFn4_18(inp, wk, rk):
    x0 = inp[0]
    x1 = xor_(inp[1], wk[0])
    x2 = inp[2]
    x3 = xor_(inp[3], wk[1])
    for i in range(18):

        x1 = xor_(x1, (f0(x0, rk[2*i])))

        x3 = xor_(x3, (f1(x2, rk[2*i+1])))

        temp = x0
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = temp
    return x0, x1, x2, x3
