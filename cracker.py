
import allfunctions
 

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'qwerty123'
actual_password_hash = allfunctions.hash(actual_password)
 
wordlist = allfunctions.readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
allfunctions.bruteforce(guesspasswordlist, actual_password_hash)
 
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")