import string
import secrets
import random
from termcolor import colored

if __name__ == '__main__':
	pass_lenght = input('How long should be the password ? (We recomand more then "50") : ')
	int_pass_lenght = int(pass_lenght)
	if int_pass_lenght >= 25:
		print('We need a secret key , it can be anything. You wont be able to decrypt the password from the key.')
		print('Example: ImHungryToday 14')
		digits_count = (int_pass_lenght / 2)
		int_digits_count = int(digits_count)
		password = input('Tell me your secret key to encrypt : ')
		alphabet = string.ascii_letters + string.digits + string.punctuation
		while True:
			   password = ''.join(secrets.choice(alphabet) for i in range(int_pass_lenght))
			   x = (random.randint(8, int_digits_count))
			   if (any(c.islower() for c in password)
			           and any(c.isupper() for c in password)
			           and sum(c.isdigit() for c in password) >= x):
			       break
		print (colored('Your new password : ', 'red'))        
		print(password)
	else:
		print('Password is to short ')	
	
	
