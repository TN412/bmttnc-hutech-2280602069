import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate() #Tao khoa rieng tu
        vk = sk.get_verifying_key() #Tao khoa cong khai tu khoa rieng tu

        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, sk):
        return sk.sign(message.encode('ascii')) #Ky du lieu bang khoa rieng tu

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:    
            return vk.verify(signature, message.encode('ascii')) #Xac thuc chu ky
        except ecdsa.BadSignatureError:
            return False