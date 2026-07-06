import os
import base64

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



def create_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )


    return base64.urlsafe_b64encode(
        kdf.derive(
            password.encode()
        )
    )



def encrypt_data(data,password):

    salt = os.urandom(16)

    key=create_key(
        password,
        salt
    )

    return (
        salt,
        Fernet(key).encrypt(data)
    )



def decrypt_data(
        data,
        password,
        salt
):

    key=create_key(
        password,
        salt
    )

    return Fernet(
        key
    ).decrypt(
        data
    )