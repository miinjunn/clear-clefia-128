import time
import os

lokasi = 'python D:/Kuliah/"SMT XI (terakhir)"/"Skripsi XI"/"Clefia-128 python"/clefia_encrypt_file.py'


def repeat(path, iter):
    temp = []
    i = 0
    while i < iter:
        print(i)
        start = time.time()
        os.system(path)
        end = time.time()
        waktu = end - start
        temp.append(waktu)
        i += 1
    return temp


coba = repeat(path=lokasi, iter=100)

print(f"waktu total \t: {coba}")
print(f"rata-rata \t: {sum(coba)/len(coba)}")
