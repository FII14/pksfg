import os
import time
import argparse
import subprocess

file = input("Enter the path to the steghide file: ")

wordlist = input("Enter the path to the wordlist: ")


try:
    with open(wordlist, 'r') as wordlist_file:
        for line in wordlist_file:
            password = line.strip()
            command = ['steghide', 'extract', '-sf', file, '-p', password, '-f']
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                cracked_file = f"{file}.out"
                command_s = ['steghide', 'extract', '-sf', file, '-p', password, '-xf', cracked_file]
                subprocess.run(command_s, capture_output=True, text=True)
                print(f"{p}[{c}{now.strftime('%H:%M:%S')}{p}] [{g}INFO{p}] {pb}Cracked file saved as: {g}{cracked_file}{p}")
                break
            else:
                print(f"{p}[{c}{now.strftime('%H:%M:%S')}{p}] [{gb}INFO{p}] {p}Incorrect password: {r}{password}{p}")

        else:
            print(f"\n{r}[-] {p}No matching password found in the wordlist.")

except Exception as e:
    print(f"{r}[-] {p}An error occurred: {str(e)}")
