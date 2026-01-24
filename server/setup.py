import scrypt
import os.path
import os
print("welcome to swffy setup")
print("please enter a password for the admin panel!! this is where you approve/reject flash stuff")
pw = input()
encrypted = scrypt.encrypt(pw, pw)
with open("adminpw.bin", "wb") as f:
    f.write(encrypted)
    print("password written and encrypted! have fun")
ftm = ["db", "db/swf", "db/torrents", "db/swfnames", "db/lid"]
for item in ftm:
    if not os.path.exists(item):
        os.mkdir(item)
        print("folders required werent found and were made!")