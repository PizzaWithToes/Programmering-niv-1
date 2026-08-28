import secrets
import string

length = 8
random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
print(random_string)