from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_data(plaintext:bytes,key:bytes) -> bytes:
    iv= get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    padded_data=pad(plaintext,AES.block_size)
    encrypted_data=cipher.encrypt(padded_data)
    return iv+encrypted_data

def decrypt_data(encrypted_data:bytes,key:bytes)->bytes:
    iv=encrypted_data[:16]
    encrypted_data=encrypted_data[16:]
    cipher=AES.new(key,AES.MODE_CBC,iv)
    padded_data=cipher.decrypt(encrypted_data)
    plaintext=unpad(padded_data,AES.block_size)
    return plaintext

def read_file(file_path : str) -> bytes:
    with open(file_path,'rb') as f:
        return f.read()
    
def write_file(file_path : str, data: bytes)-> bytes:
    with open(file_path,'wb') as f:
        f.write(data)

def main():
    key=b'this is key123'

    og_content=read_file("example.txt")
    print("original contenet :")
    print(og_content.decode())

    encrytped_text=encrypt_data(og_content,key)   
    print("encrypted data : ")
    print(encrytped_text.hex())

    dencrytped_text=decrypt_data(encrytped_text,key)   
    print("decrypted data : ")
    print(dencrytped_text.decode())

    write_file('encrypted_example.bin',encrytped_text)
    write_file('decrypted_example.txt',dencrytped_text)

if __name__ =="__main__":
    main()    



