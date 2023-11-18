from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
BLOCK_SIZE = 8 # bytes, used for padding

def encrypt_text():
    print("Encrypting Text:\n")

    # Create new Random key
    key = get_random_bytes(8) 
    key_file = open('Kim_DES_Key.bin', 'wb') 
    key_file.write(key)
    key_file.close()

    # Read plaintext file
    read_file_name = input("Enter Input File Name: ")
    print("\n")

    text_file = open(read_file_name, 'rb')
    plaintext = text_file.read()
    text_file.close()

    # Encrypt the plaintext
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    # print("Ciphertext:", ciphertext)

    # Write ciphertext into output file
    cipher_file = open('Kim_DES_Ciphertext', 'wb')
    cipher_file.write(ciphertext)
    cipher_file.close()
    
def decrypt_text():
    print("Decrypting Text:\n")

    # Retrieve ciphertext
    cipher_file_name = input("Enter Input Ciphertext File Name: ")
    cipher_file = open(cipher_file_name, 'rb') 
    ciphertext = cipher_file.read()
    cipher_file.close()

    # Retrieve key from key file
    key_file_name = input("Enter Key File Name: ")
    key_file = open(key_file_name, 'rb') 
    retrieved_key = key_file.read()
    key_file.close()

    # Decipher Text and write in output file
    decipher = DES.new(retrieved_key, DES.MODE_ECB)
    decrypted_text = decipher.decrypt(ciphertext).decode()
    # print("Decrypted Text:", decrypted_text)
    
    output_file = open('output_text', 'w', encoding="utf-8")
    output_file.write(decrypted_text)
    output_file.close()


print("Welcome to Brad's Pycryptodome Assignment\n")

option = ""

while(option == ""):
    option = input("Would you like to encrypt or decrypt: ")

    if option == "encrypt":
        encrypt_text()
        # add choose file to read from
    elif option == "decrypt":
        decrypt_text()
        # add choose file to key and ciphertext

    else:
        print("Invalid Input, try again\n")
        option = ""