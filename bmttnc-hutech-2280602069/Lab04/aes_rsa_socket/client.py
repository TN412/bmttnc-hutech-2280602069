from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib
import sys

#Initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

#Generate RSA key pair
client_key = RSA.generate(2048)

#Receive sever's public key
server_public_key = RSA.import_key(client_socket.recv(2048))

#Send client's public key to sever
client_socket.send(client_key.publickey().export_key(format='PEM'))

#Receive encrypted AES key from sever
encrypted_aes_key = client_socket.recv(2048)

#Decrypt AES key using client's private key
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Biến để kiểm soát thread nhận tin nhắn
running = True

#Function to encrypt message
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

#Function to decrypt message
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

#Function to receive message from sever
def receive_message():
    global running
    while running:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("Received: ", decrypted_message)
        except:
            break

#Star the receive message thread
receive_thread = threading.Thread(target=receive_message, daemon=True)
receive_thread.start()

#Send message from the client
try:
    while True:
        message = input("Enter message: ('exit' to quit): ")
        if message == 'exit':
            encrypted_message = encrypt_message(aes_key, message)
            client_socket.send(encrypted_message)
            print("Đang thoát chương trình...")
            break
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.send(encrypted_message)
finally:
    #Dọn dẹp và đóng kết nối
    running = False
    client_socket.close()
    sys.exit(0)