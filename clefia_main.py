from fungsi import xor_, f0, f1, gFn4_18, break_input, con128, redefine_con128, generate_rk, gFn4_12, gFn4_18

# 16 char
plaintext = "abcdefghijkl"
plain = break_input(plaintext)
print(f"plaintext\t: {plaintext}")
print(f"plain break\t: {plain}")
# -----------------~~~~~~-----------------
border: str = "~~~~~~"
print(f"{border:-^40}")
# -----------------~~~~~~-----------------
# 16 char
key_user = "two one tes12"
key = break_input(key_user)
print(f"key user\t: {key_user}")
print(f"key\t\t: {key}")

# get Constant Value
con_128 = redefine_con128(con128)


# -----------------~~~~~~-----------------
# create ENC-functionF
def encrypt(plain, key):

    # generate L
    l0, l1, l2, l3 = gFn4_12(key, con_128)
    l_key = l3 + l0 + l1 + l2
    print(f"L \t\t: {l_key}")

    # Expanding K and L to generate round-key
    keyz = key[0] + key[1] + key[2] + key[3]
    rk = generate_rk(key=keyz, L=l_key, constant_value=con_128)
    for i in range(len(rk)):
        print(f"rk{i} \t\t: {rk[i]}")

    # generate ciphertext
    c0, c1, c2, c3 = gFn4_18(plain, key, rk)
    cipher = c3 + (xor_(c0, key[2])) + c1 + (xor_(c2, key[3]))
    cipher_hex = [hex(i)[2:] for i in cipher]
    return cipher_hex


# -----------------~~~~~~-----------------F
print(f"{border:-^40}")
enc = encrypt(plain=plain, key=key)
print(f"ciphertext \t: {enc}")
print(f"len cipher \t: {len(enc)}")
for i in enc:
    print(i, end='')
