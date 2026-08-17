# haikal-sec ( make this at 5am *cuz i cant sleep lol)
import getpass
import time
from art import tprint

if __name__ == "__main__":
    print("=" * 90)
    tprint("    Casino Account     ")
    print("=" * 90)

urname = input('What is your name: ')
print(f'SYSTEM:Nice to meet you {urname}!')
username = input('Enter your username: ')
password = getpass.getpass('Enter password: ')
print('Processing Verified...')
time.sleep(5)

if username == 'npc123' and password == 'notnpc123':
    print('Access Granted!')
    bankAccount = input('How many you wanna to topup: $')
    gambling = input('How many you wanna gamble: $')
    balanceAccount = int(bankAccount) - int(gambling)
else: 
    print('Access Denied!')

if balanceAccount > 0:
    print(f'Nice! your current balance: ${balanceAccount}')   

else: 
    balanceAccount <= 0
    tprint('loser')
    print(f'Loser! your current balance: ${balanceAccount}')