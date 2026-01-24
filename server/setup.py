import scrypt
print("welcome to swffy setup")
print("please enter a password for the admin panel!! this is where you approve/reject flash stuff")
pw = input()
encrypted = scrypt.encrypt(pw, pw)
with open("adminpw.bin", "wb") as f:
    f.write(encrypted)
    print("password written and encrypted! have fun")