import scrypt

h = scrypt.encrypt("balls", "balls")
scrypt.decrypt(h, "no")