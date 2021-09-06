from fernet_cryptography import *

if __name__ == "__main__":
    if STRING_CRYPTOGRAPHY == "":
        print(
            {
                'statusCode': 500,
                'body': {'Result': 'Transaction error!'}
            }
        )
    else:
        print(
            {
                'statusCode': 200,
                'body': {'Result': 'Decryption OK!'}
            }
        )
