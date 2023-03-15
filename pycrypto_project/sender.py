import os
import socket

from Crypto.Cipher import AES

key = b"AbdullahAbdullah"
nonce = b"PasswordPassword"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_size = os.path.getsize("file")
print(f'File Size = {file_size}')

with open ("file", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

client.send("newfile.txt".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")
print('Sender Runned')
client.close()