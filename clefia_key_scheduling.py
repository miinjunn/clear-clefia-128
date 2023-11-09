from fungsi import redefine_con128, f0, f1, S0, S1

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

# plaintext                00010203 04050607 08090a0b 0c0d0e0f
# key                      ffeeddcc bbaa9988 77665544 33221100
# L                        8f89a61b 9db9d0f3 93e65627 da0d027e
# ciphertext               de2bf2fd 9b74aacd f1298555 459494fd


# generating L form K
key = [0xff, 0xee, 0xdd, 0xcc,
       0xbb, 0xaa, 0x99, 0x88,
       0x77, 0x66, 0x55, 0x44,
       0x33, 0x22, 0x11, 0x00]


con_128 = redefine_con128(con128)
# ----------------------------------------------------------------------------------------

key = [int(hex(i)[2:], base=16) for i in key]
# print(key)

k_as_input = []
for i in range(4):
    k_as_input.append(key[i*4:i*4+4])

x0, x1, x2, x3 = k_as_input
# print(f"x0: {x0}")
# print(f"x1: {x1}")
# print(f"x2: {x2}")
# print(f"x3: {x3}")


# ----------------------------------------------------------------------------------------
# Generate L from K:

# create GFN_4,12 function:
# seperti gfn biasa, bedanya:
# - RK[i] diganti dengan con_128[i]
# - Key jadi input


def xor_(state1, state2):
    temp = []
    for i in range(len(state1)):
        temp.append(state1[i] ^ state2[i])
    return temp


# tes = xor_(x1, (f0(x0, con_128[0])))
# tes = f0(x0, con_128[0])
# print(f"tes: {tes}")


def gFn4_12(inp0, inp1, inp2, inp3):
    x0 = inp0
    x1 = inp1
    x2 = inp2
    x3 = inp3
    for i in range(12):

        x1 = xor_(x1, (f0(x0, con_128[2*i])))

        x3 = xor_(x3, (f1(x2, con_128[2*i+1])))

        temp = x0
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = temp
    return x0, x1, x2, x3


l0, l1, l2, l3 = gFn4_12(x0, x1, x2, x3)
# disusun spt ini karena pada round-12 tidak ada swap
l_key = l3 + l0 + l1 + l2
l_key_hex = [hex(i)[2:] for i in l_key]
# print("----------------------------------------------------------------------------------")
# print("L (intermediate key): ")
# print(l_key)
# print(l_key_hex)
# print("----------------------------------------------------------------------------------")


# # round-2
# x02 = y0
# x12 = f0(x02, con_128[2])
# x22 = y2
# x32 = f1(x22, con_128[3])

# y02 = x12
# y12 = x22
# y22 = x32
# y32 = x02


# ----------------------------------------------------------------------------------------
# Expanding K and L

keyz = x0 + x1 + x2 + x3
# print(f"key: {keyz}")

# perlu bikin fungi double_swap -> sigma(l_key)


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


rk = []
for i in range(9):
    T = xor_(l_key, (con_128[4*i + 24] + con_128[4*i + 25] +
             con_128[4*i + 26] + con_128[4*i + 27]))
    l_key = sigma(l_key)
    if i % 2 != 0:
        T = xor_(T, keyz)
    # print(f"RK{i}: {T}")
    # for k in range(len(T)):             # convert dec to hex
    #     T[k] = hex(T[k])[2:]
    # print(f"RK{i}: {T}")
    for j in range(4):
        rk.append(T[j*4: j*4+4])


# print(rk)
# for i in range(len(rk)):
#     print(f"rk{i}: {rk[i]}")
