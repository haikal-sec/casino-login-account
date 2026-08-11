# haikal-sec ( make this at 5am *cuz i cant sleep lol)
import time
import getpass
from art import tprint

tprint('NPC CASINO!')
urname = input('What is your name: ')
print(f'Nice to meet you {urname}!')
username = input('Enter your username: ')
password = getpass.getpass('Enter password: ')
print('Processing Verified...')
time.sleep(5)

if username == 'npc123' and password == 'notnpc123':
    print('Access Granted!')
    bankAccount = input('How many you wanna to topup: ')
    gambling = input('How many you wanna gamble: ')
    balanceAccount = int(bankAccount) - int(gambling)
    tprint('loser')
    print(f'Loser! your current balance: {balanceAccount}')
else: 
    print('Access Denied!')
