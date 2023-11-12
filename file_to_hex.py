
import binascii


# file to hex
with open('baju.webp', 'rb') as fp:
    hexstring = binascii.hexlify(fp.read())

# print(hexstring)
print(type(hexstring))
print(len(hexstring))

# print(hexstring)
to_hex = hexstring.decode("ascii")
# print(to_hex)
print(type(to_hex))
print(len(to_hex))

# panjang = len(hexstring)
# print(panjang)

# masukan = panjang // 16
# print(f"masukan: {masukan}")

# hasil = masukan * 16
# print(f"hasil: {hasil}")


# with open('new.webp', 'wb') as fp:
#     fp.write(binascii.unhexlify(to_hex))

# -------------------------------------------------------------------------------------

# halo = 'halosemua'
# print(halo)
# halo = [hex(ord(i))[2:] for i in halo]
# print(halo)

# haloh = ''
# for i in halo:
#     haloh += i

# print(haloh)
# print(len(haloh))


def split(state):
    split_2 = []
    for i in range(0, len(state), 2):
        split_2.append(state[i:i+2])
    return split_2


# s = split(haloh)
# print(s)
# print(len(s))

ss = split(to_hex)
# print(ss)
print(len(ss))
ss = [int(i, base=16) for i in ss]
# print(ss)
print(len(ss))

split_16 = []
for i in range(0, len(ss), 16):
    split_16.append(ss[i: i+16])

akan_diconvert = split_16


def convert_per_i(state):
    temp = [hex(i)[2:] for i in state]
    temp2 = []
    for i in temp:
        if len(i) == 1:
            i = '0' + i
        temp2.append(i)
    return temp2


def convert_semua(statex):
    semua = ''
    for i in range(len(statex)):
        temp = convert_per_i(statex[i])
        for item in temp:
            semua += item
    return semua


sem = convert_semua(akan_diconvert)
print(sem)
print(len(sem))

with open('baru.webp', 'wb') as fp:
    fp.write(binascii.unhexlify(to_hex))
