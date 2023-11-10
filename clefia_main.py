from fungsi import xor_, f0, f1, gFn4_18

# 16 char
plaintext = "abcdefghijklmno "
plaintext = [ord(i) for i in plaintext]
plaintext = [hex(i)[2:] for i in plaintext]
# print(plaintext)

# 16 char
key = ['61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '00']
key = [int(i,base=16) for i in key]
# key = [hex(i)[2:] for i in key]
print(key)

# create ENC-functionF
def encript(plain, key):
    pass
