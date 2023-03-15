#https://www.youtube.com/watch?v=wJanjCfyhAk
from Crypto.Cipher import AES

key = b"AbdullahAbdullah"
nonce = b"PasswordPassword"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext = cipher.encrypt(b"Hello World!")

print(ciphertext)

chiper = AES.new(key, AES.MODE_EAX, nonce)
print(chiper.decrypt(ciphertext))