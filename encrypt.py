from hashlib import sha256

while 1:
  password = input('Enter a password to encrypt: ')
  print(sha256(password.encode()).hexdigest())
