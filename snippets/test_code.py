# I will use this code snippet as a sample

frist_name = "Julie"
last_name = "Blevins"

def account_generator(frist_name, last_name):
	account_name = frist_name[:3] + last_name[:3]
	return account_name
	
new_account = account_generator(frist_name, last_name)

print(new_account)