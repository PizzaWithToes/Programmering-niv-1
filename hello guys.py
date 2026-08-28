import random
import string

randomNumber = random.randint(1,10)
print(randomNumber)

length = 5
randomString = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

if randomNumber >= 5:
    print(str(randomString) + str(randomNumber))
else:
    print("hejDÅ")