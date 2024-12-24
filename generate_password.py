import hashlib 
import random
import json
import string

def generatePassword():
    password="".join(
        random.choices(string.ascii_letters + string.digits ,k =random.randint(8,16))
    )
    print(f"Oluşturulan şifre: {password}")
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return password, hashed_password

plain_password, hashed_password = generatePassword()
print(f"MD5 Hash: {hashed_password}")