import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation
print(''.join(secrets.choice(chars) for i in range(40))) #40 = length