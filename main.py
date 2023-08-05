import gnupg
import os
import sys

gpg = gnupg.GPG()

file_gpg = input("Masukkan nama file GPG: ")

if not os.path.exists(file_gpg):
    print(f"Kesalahan: File gpg '{file_gpg}' tidak ditemukan.")
    sys.exit(1)

file_wordlist = input("Masukkan nama file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.")
    sys.exit(1)

with open(file_wordlist, "r", encoding="latin-1", error="ignore") as f:
    daftar_kata_sandi = f.read().splitlines()

for kata_sandi in daftar_kata_sandi:
    print(f"Mencoba kata sandi: {kata_sandi}")

    with open(filename, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=passphrase)
        if decrypted_data.ok:
            print('Berhasil mendekripsi file.')
            print(decrypted_data.data)
            break
        # else:
        #    print('Gagal mendekripsi file.')
