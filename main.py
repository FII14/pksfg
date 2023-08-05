import os
import time
import subprocess

file_stegano = input("Enter the path to the steghide file: ")

file_wordlist = input("Enter the path to the wordlist: ")


try:
    with open(file_wordlist, 'r') as w:
        for baris in w:
            kata_sandi = baris.strip()
            command = ['steghide', 'extract', '-sf', file_stegano, '-p', kata_sandi, '-f']
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                cracked_file = f"{file}.out"
                command_s = ['steghide', 'extract', '-sf', file, '-p', password, '-xf', cracked_file]
                subprocess.run(command_s, capture_output=True, text=True)
                print(f"\n[*] File zip: {file_zip}\n[*] Kata sandi: {password}\n[*] Status: Benar\n")
                break
                sys.exit(0)
            else:
                print(f"\n[*] File zip: {file_zip}\n[*] Kata sandi: {password}\n[*] Status: Salah")
        else:
            print(f"Kata sandi tidak ditemukan dalam file wordlist '{file_wordlist}'.")
            sys.exit(1)
            
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    sys.exit(1)
