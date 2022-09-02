import string
import secrets
import random
import argparse
from termcolor import colored

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Password generator')
	parser.add_argument('-l', '--len', type = int, required = False, help = 'Password lenght, it needs to be longer then 25 characters.')
	parser.add_argument('-w', '--wrd', type = str, required = False, help = 'We need a word that will be used to encrypt your password, you wont be able to decrypt the password from the word back !!.')
	args = parser.parse_args()
	lenght = args.len
	word = args.wrd
	if lenght and word:
		int_pass_lenght = int(lenght)
		password = word
		if int_pass_lenght >= 25:
			digits_count = (int_pass_lenght / 2)
			int_digits_count = int(digits_count)
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

	else:	
		pass_lenght = input('How long should be the password ? (We recomand more then "50") : ')
		int_pass_lenght = int(pass_lenght)
		if int_pass_lenght >= 25:
			digits_count = (int_pass_lenght / 2)
			int_digits_count = int(digits_count)
			print('We need a secret key , it can be anything. You wont be able to decrypt the password from the key.')
			print('Example: ImHungryToday 14')
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
	
	
