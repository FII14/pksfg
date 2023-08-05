import subprocess
import os
import sys
import time

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Pemecah Kata Sandi File Steganografi    @
@ Pembuat : Rofi [FII14]                            @
@ GitHub  : https://github.com/FII14/PKSFS          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

file_steganografi = input("Masukkan nama file steganografi: ")

if not os.path.exists(file_steganografi):
    print(f"Kesalahan: File steganografi '{file_steganografi}' tidak ditemukan.")
    sys.exit(1)

file_wordlist = input("Masukkan nama file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.")
    sys.exit(1)

try:
    with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as daftar_kata_sandi:
        for kata_sandi in daftar_kata_sandi:
            kata_sandi = kata_sandi.strip()
            perintah = ["steghide", "extract", "-sf", file_steganografi, "-p", kata_sandi, "-f"]
            hasil = subprocess.run(perintah, capture_output=True, text=True, encoding="utf-8")

            if hasil.returncode == 0:
                file_terpecahkan = f"{file_steganografi}.out"
                perintah_extract = ["steghide", "extract", "-sf", file_steganografi, "-p", kata_sandi, "-xf", file_terpecahkan]
                hasil_extract = subprocess.run(perintah_extract, capture_output=True, text=True, encoding="utf-8")

                if hasil_extract.returncode == 0:
                    print(f"\n[*] File Terpecahkan: {file_terpecahkan}\n[*] Kata Sandi: {kata_sandi}\n[*] Status: Benar\n")
                    break
            else:
                print(f"\n[*] File Steganografi: {file_steganografi}\n[*] Kata Sandi: {kata_sandi}\n[*] Status: Salah")
            time.sleep(1)
        else:
            print(f"Kata sandi tidak ditemukan dalam file wordlist '{file_wordlist}'.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    
