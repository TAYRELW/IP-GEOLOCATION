import requests
import os
os.system('figlet TAYRELW')
a = input ('DIGITE O IP: ')
b = requests.get("http://ip-api.com/xml/{}".format(a))
print(b.text)