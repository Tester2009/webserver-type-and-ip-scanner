"""
Hello . This code written by Muhammad Aliff Muazzam bin Jaafar .
Feel free to checkout .
Built with love <3 .

http://www.facebook.com/Tester2009
https://github.com/alepcat1710
http://www.twitter.com/mambj2009
http://kamisukagodam.blogspot.com
muhammadaliffmuazzam@gmail.com || tester2009.hakase@gmail.com
- Tester2009 - Alpha Maurice Production -

Feel free to use . Do not change copyright, mastah !

reference
header 		: http://docs.python-requests.org/en/latest/
string replace 	: http://www.tutorialspoint.com/python/string_replace.htm
clear console 	: http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console
find string 	: http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-method
"""

import requests
import socket
import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == ('ce', 'nt', 'dos'):
        os.system('cls')
clear()
print "          _       _             __  __                  _            _____               _            _   _             "
print "    /\   | |     | |           |  \/  |                (_)          |  __ \             | |          | | (_)            "
print "   /  \  | |_ __ | |__   __ _  | \  / | __ _ _   _ _ __ _  ___ ___  | |__) | __ ___   __| |_   _  ___| |_ _  ___  _ __  "
print "  / /\ \ | | '_ \| '_ \ / _` | | |\/| |/ _` | | | | '__| |/ __/ _ \ |  ___/ '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ "
print " / ____ \| | |_) | | | | (_| | | |  | | (_| | |_| | |  | | (_|  __/ | |   | | | (_) | (_| | |_| | (__| |_| | (_) | | | |"
print "/_/    \_\_| .__/|_| |_|\__,_| |_|  |_|\__,_|\__,_|_|  |_|\___\___| |_|   |_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|"
print "           | |                                                                                                          "
print "           |_|                                                                              simple tool from Tester2009 "
print "                                               -|| Get your webserver type and IP ||-                                   "
print "Github: https://github.com/alepcat1710"
print "Facebook: https://facebook.com/Tester2009"
print "Twitter: https://twitter.com/mambj2009"
url=raw_input("Enter website URL: ")

# okay. now start if string contain 'http://'
if "http://" in url:
	req = requests.get(url)
	req_header = req.headers['server']
	replace_1 = url.replace("http://", "");
	ip_1 = socket.gethostbyname(replace_1)
	print "Target: " +url
	print "Server: " +req_header
	print "IP: " +ip_1
	print "Done !"
elif "https://" in url:
	req_2 = requests.get(url)
	req_header_2 = req_2.headers['server']
	replace_2 = url.replace("https://", "");
	ip_2 = socket.gethostbyname(replace_2)
	print "Target: " +url
	print "Server: " +req_header_2
	print "IP: " +ip_2
	print "Done !"
else:
	req_3 = requests.get("http://" +url)
	req_header_3 = req_3.headers['server']
	ip_3 = socket.gethostbyname(url)
	print "Target: " +url
	print "Server: " +req_header_3
	print "IP: " +ip_3
	print "Done !"
