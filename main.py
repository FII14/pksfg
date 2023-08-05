import gnupg
import os
import sys

gpg = gnupg.GPG()

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Pemecah Kata Sandi File GPG    @
@ Pembuat : Rofi [FII14]                   @
@ GitHub  : https://github.com/FII14/PKSFG @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

file_gpg = input("Masukkan nama file GPG: ")

if not os.path.exists(file_gpg):
    print(f"Kesalahan: File GPG '{file_gpg}' tidak ditemukan.")
    sys.exit(1)

file_wordlist = input("Masukkan nama file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.")
    sys.exit(1)

with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as f:
    daftar_kata_sandi = f.read().splitlines()

for kata_sandi in daftar_kata_sandi:
    print(f"\n[*] File GPG: {file_gpg}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Salah")
    with open(file_gpg, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=kata_sandi)
        if decrypted_data.ok:
            print(f"\n[*] File GPG: {file_gpg}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Benar\n")
            sys.exit(0)

print(f"Kata sandi tidak ditemukan dalam file wordlist '{file_wordlist}'.")
