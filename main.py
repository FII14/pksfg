import gnupg

gpg = gnupg.GPG()

filename = input("Masukkan nama file GPG: ")
wordlist_file = input("Masukkan nama file wordlist: ")

with open(wordlist_file, 'r') as f:
    wordlist = f.read().splitlines()

for passphrase in wordlist:
    print(f"Mencoba kata sandi: {passphrase}")

    with open(filename, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=passphrase)
        if decrypted_data.ok:
            print('Berhasil mendekripsi file.')
            print(decrypted_data.data)
            break
        else:
            print('Gagal mendekripsi file.')
