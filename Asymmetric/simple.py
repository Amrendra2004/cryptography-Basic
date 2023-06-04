from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Create a Fernet symmetric encryption object
cipher_suite = Fernet(key)

# Encrypt a message
message = b"Hello, encryption!"
ciphertext = cipher_suite.encrypt(message)

# Print the ciphertext
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_message = cipher_suite.decrypt(ciphertext)

# Print the decrypted message
print("Decrypted message:", decrypted_message)
