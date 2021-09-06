from cryptography.fernet import Fernet

# STRING_CRYPTOGRAPHY = "Contains encrypted message"
STRING_CRYPTOGRAPHY = ""
ENCODING = 'utf-8'


def main():
    print("Starting keys...")
    # Generating key to client that need to encrypt and decrypt
    key = Fernet.generate_key()
    print("Generated Key: %s" % key.decode(ENCODING))

    # Creating object to manipulate string
    f = Fernet(key)

    # Generating encrypt message
    token = f.encrypt(STRING_CRYPTOGRAPHY.encode(ENCODING))
    print("Encrypt Message: %s" % token)

    # Decrypt message
    clean_message = f.decrypt(token)
    print("Decrypt Message: %s" % clean_message.decode(ENCODING))
