from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os


def encrypt_file(input_file, output_file, key):
    """Encrypt the contents of a file using AES."""
    try:
        # Read the content of the file
        with open(input_file, "rb") as f:
            plaintext = f.read()

        # Initialize AES cipher
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        # Write the encrypted data (including the IV) to the output file
        with open(output_file, "wb") as f:
            f.write(cipher.iv)  # Prepend the IV
            f.write(ciphertext)

        print(f"File '{input_file}' encrypted successfully to '{output_file}'")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")


def decrypt_file(input_file, output_file, key):
    """Decrypt the contents of a file encrypted with AES."""
    try:
        # Read the encrypted content of the file
        with open(input_file, "rb") as f:
            iv = f.read(16)  # Read the first 16 bytes (IV)
            ciphertext = f.read()

        # Initialize AES cipher for decryption
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Write the decrypted data to the output file
        with open(output_file, "wb") as f:
            f.write(plaintext)

        print(f"File '{input_file}' decrypted successfully to '{output_file}'")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")


# Generate a random AES key for testing (save this securely in real-world use!)
if __name__ == "__main__":
    key = get_random_bytes(16)  # Generate a 16-byte key

    # Example files for testing (update file paths as needed)
    input_file = "current_weather.csv"
    encrypted_file = "current_weather_encrypted.bin"
    decrypted_file = "current_weather_decrypted.csv"

    if os.path.exists(input_file):
        # Encrypt the input file
        encrypt_file(input_file, encrypted_file, key)

    if os.path.exists(encrypted_file):
        # Decrypt the encrypted file
        decrypt_file(encrypted_file, decrypted_file, key)
