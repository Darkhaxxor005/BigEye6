import sys
import time
import os


print (''' 
                                @                           @/              
                            @@@                               @@@           
                        %@@@                                   @@@.        
                      @@@@@                                     @@@@%      
                     @@@@@                                       @@@@@     
                    @@@@@@@                  @                  @@@@@@@    
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@    
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@     
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@       
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@           
                                  @@@   @@@@@@@@@@@   @@@                  
                                 @@@@*  ,@@@@@@@@@(  ,@@@@                 
                                 @@@@@@@@@@@@@@@@@@@@@@@@@                 
                                  @@@.@@@@@@@@@@@@@@@ @@@                  
                                    @@@@@@ @@@@@ @@@@@@                    
                                       @@@@@@@@@@@@@                       
                                       @@   @@@   @@                       
                                       @@ @@@@@@@ @@                       
                                         @@% @  @@                 


                           /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$ 
                          /$$__  $$| $$  | $$| $$  | $$ /$$__  $$
                         | $$  \__/| $$  | $$| $$  | $$| $$  \__/
                         | $$ /$$$$| $$$$$$$$| $$$$$$$$| $$      
                         | $$|_  $$| $$__  $$| $$__  $$| $$      
                         | $$  \ $$| $$  | $$| $$  | $$| $$    $$
                         |  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/
                          \______/ |__/  |__/|__/  |__/ \______/ 
                                                                Coded By =>>R00t Dev1l /// Modules by =>> k0w581k
                                        Join Our Facebook Group =>>https://www.facebook.com/groups/grayhathackerscommunity
                                        
                                        

''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("\033[32m=>>> Loading (Please Wait.....)  ")
time.sleep(1)
os.system('clear')

def linkgrabber():
	import os
	import time
	from collections import deque
	from urllib.parse import urlsplit
	import requests
	from bs4 import BeautifulSoup

	R = "\033[1;31m"            #
	B = "\033[1;34m"            #
	Y = "\033[1;33m"            #
	G = "\033[32m"              #
	RS = "\033[0m"              #
	W = "\033[1;37m"            #

	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mDomain \033[0m" + R + "Link " + Y + "Grabber " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print(" ")
	target = input("" + RS + "[" + B + " ENTER " + R + "Domain " + RS + "]" + G + ": " + RS).lower()
	os.system("reset")
	print("\n"+R+"Scanning "+Y+"Link Grabber "+R+" : " + RS + target)
	time.sleep(2)
	if not (target.startswith("http://") or target.startswith("https://")):
	    target = "http://" + target
	deq = deque([target])
	pro = set()
	
	try:
	    while len(deq):
	        url = deq.popleft()
	        pro.add(url)
	        parts = urlsplit(url)
	        base = "{0.scheme}://{0.netloc}".format(parts)
	
	        print("[✌] Find URL " + "\033[34m" + url + "\033[0m")
	        try:
	            response = requests.get(url)
	        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	            continue
	
	        soup = BeautifulSoup(response.text, "lxml")
	        for anchor in soup.find_all("a"):
	            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
	            if link.startswith("/"):
	                link = base + link
	            if not link in deq and not link in pro:
	                deq.append(link)
	            continue
	
	except KeyboardInterrupt:
	    print("\n")
	    print("[-] User Interruption Detected..!")
	    time.sleep(1)
	    print("\n \t\033[34m[!] I like to See Ya, Hacking Anywhere ..!\033[0m\n")


	except Exception:
	    pass
		
def dnsmap():
	import os
	import subprocess
	
	R = " \033[1;31m"
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"
	G = "\033[32m"
	W = "\033[1;37m"
	
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m\033[0m" + R + "DNS " + Y + "MAP " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	target = input("\n"+W+"["+R+"Domain "+W+"]"+G+": "+RS)
	subprocess.check_call(['dnsmap', target])
	
def ipscan():
	import json
	import os
	import sys
	import time
	import urllib.request
	
	
	R = " \033[1;31m"	
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"	
	G = "\033[32m"
	W = "\033[1;37m"
	
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mIP\033[0m" + R + "Address " + Y + "information " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print(" ")
	target = input(W+"["+R+"IP "+W+"]"+G+": "+RS)
	url = ("http://ip-api.com/json/")
	response = urllib.request.urlopen(url + target)
	data = response.read()
	jso = json.loads(data)
	time.sleep(0.5)
	
	print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
	print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")
	
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mWhois Lookup\033[0m" + R + "By " + Y + "IP " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print(" ")
	command = ("whois " + target)
	proces = os.popen(command)
	results = str(proces.read())
	print("\033[0m" + results + "\033[0m")
	

def whoisdomainscan():
	import os
	import time

	R = " \033[1;31m"
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"
	G = "\033[32m"
	W = "\033[1;37m"
	
	
	os.system("clear")
	print(" ")
	target = input(W+"["+R+"Domain "+W+"]"+G+": "+RS)
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mWhois Lookup\033[0m" + R + "By " + Y + "Domain " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m".format(target) + target)
	print(" ")
	time.sleep(0.5)
	command = ("whois " + target)
	proces = os.popen(command)
	results = str(proces.read())
	print("\033[0m" + results + "\033[0m")

def robottxtscan():
	#!/usr/bin/env/python3

	import sys
	from urllib.error import URLError
	import dns.resolver  # Installed packages: 'dnspython'
	import json
	import subprocess
	import time
	import urllib.request
	import os
	from time import gmtime, strftime
	from urllib.error import URLError
	from urllib.parse import urlsplit
	import urllib.request
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	
	#############################
	#    COLORING YOUR SHELL    #
	#############################
	R = "\033[1;31m"            #
	B = "\033[1;34m"            #
	Y = "\033[1;33m"            #
	G = "\033[32m"              #
	RS = "\033[0m"              #
	W = "\033[1;37m"            #
	#############################
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mRobots\033[0m" + R + "TXT " + Y + "Scanner " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print(" ")
	target = input(W+"["+R+" Domain "+W+"]"+G+": "+RS)
	print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
	print(" ")
	time.sleep(0.5)
	
	if not (target.startswith("http://") or target.startswith("https://")):
	    target = "http://" + target
	robot = target + "/robots.txt"
	
	try:
	    bots = urlopen(robot).read().decode("utf-8")
	    print("\033[37m" + (bots) + "\033[0m")
	except URLError:
	    print("\033[1;31m[-] Can\'t access to {page}!\033[1;m".format(page=robot))
	
	except Exception as ex:
	    print("\033[1;34mException caught: " + str(ex))

def whatweb():
	import os
	import subprocess
	
	
	R = "\033[1;31m"
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"
	G = "\033[32m"
	W = "\033[1;37m"
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[0m" + R + "Domain " + Y + "information " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print("\n"+W+" Note : "+R+"Type Domain With out "+G+"www "+Y+"or "+G+"https "+Y+"or "+G+"https "+RS)
	print("\n"+W+" Example : "+G+"example.com"+RS)
	target = input("\n"+W+"["+R+" Domain "+W+"]"+G+": "+RS)
	subprocess.check_call(["whatweb", target])

def httpheader():
	import time
	import os
	
	R = " \033[1;31m"
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"
	G = "\033[32m"
	W = "\033[1;37m"
	
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mHTTP\033[0m" + R + "Header " + Y + "Grabber " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	target = input("\n"+W+"["+R+"Domain "+W+"]"+G+": "+RS)
	https_or_http = input("\n\033[1;31m[\033[1;33m!\033[1;31m]\033[0m \033[1;33mHTTPS\033[0m\033[1;34m Or\033[1;33m HTTP\033[1;31m[\033[1;33m!\033[1;31m]\033[1;31m: \033[0m")
	print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
	print(" ")
	time.sleep(1.5)
	command = (https_or_http + " -v " + target)
	proces = os.popen(command)
	results = str(proces.read())
	print("\033[0m" + results + "\033[0m")

def dnsrecon():
	import os
	import subprocess

	R = " \033[1;31m"
	B = "\033[1;34m"
	Y = "\033[1;33m"
	RS = "\033[0m"
	G = "\033[32m"
	W = "\033[1;37m"
	
	
	os.system("clear")
	print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mDns\033[0m" + R + "And " + Y + "Enumerating SRV Records " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	print(" ")
	target = input(W+"["+R+"Domain "+W+"]"+G+": "+RS)
	subprocess.check_call(['dnsrecon',"-d", target])

def clickjackingtest():
	#!/usr/bin/env/python3

	import time
	import os
	
	
	#############################
	R = "\033[1;31m"            #
	B = "\033[1;34m"            #
	Y = "\033[1;33m"            #
	G = "\033[32m"              #
	RS = "\033[0m"              #
	W = "\033[1;37m"            #
	#############################
	
	os.system("clear")
	print("\n\033[1;31m[\033[1;33mi\033[1;31m]\033[0m" + R + " Clickjacking " + Y + "Test " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
	target = input("\n "+W+"["+R+"Domain "+W+"]"+G+": "+RS)
	if not (target.startswith("http://") or target.startswith("https://")):
	    target = "http://" + target
	print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m".format(target) + target)
	
	time.sleep(0.5)
	try:
	    from pip._vendor import requests
	
	    resp = requests.get(target)
	    headers = resp.headers
	    print("\nHeader set are: \n")
	    for item, xfr in headers.items():
	        print("\033[0m" + item + ":" + xfr + "\033[0")
	
	    if "X-Frame-Options" in headers.keys():
	        print("\n \033[1;31m[\033[1;33m❌\033[1;31m]\033[0m \033[1;33mClick Jacking Header is Present \033[0m")
	        print(" \033[1;31m[\033[1;33m❌\033[1;31m]\033[0m \033[1;33m! \033[1;31mYou can't clickjack this site \033[1;33m! \033[0m")
	        print(" ")
	    else:
	        facesmiling = '\U0001F600'
	        print("\n" + R + "[" + facesmiling + "]""\033[32mX-Frame-Options-Header is missing \033[1;33m! \033[1;m")
	        print(R + "[" + facesmiling + "]""\033[32mClickjacking is possible,\033[1;31mthis site is vulnerable to Clickjacking\033[1;m\n")
	        print(" ")
	except Exception as ex:
	    print("\033[1;34mException caught: " + str(ex)) 

def adminpanel():
	import urllib.request
	import os
	import time
	import sys

	print(" \033[91m YOU MUST WRITE PROTOCOLE HTTPS:// or HTTP:// (Otherwise it Won't Work) ")
	print(" \033[91m YOU MUST WRITE / AT THE END OF THE SITE.For example: www.target.com/")
	print("                                                                       ")
	url = input("\033[97m Please enter the target website URL here : ")
	print(" ")
	print ("Finding.............. : ")
	print("                                                                                        ")

	passe = ('admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
	'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
	'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
	'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
	'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
	'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
	'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
	'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
	'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
	'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
	'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
	'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
	'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
	'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
	'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
	'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
	'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
	'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
	'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
	'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
	'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
	'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
	'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
	'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
	'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
	'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
	'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
	'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
	'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
	'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
	'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
	'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
	'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
	'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
	'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
	'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
	'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
	'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
	'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
	'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
	'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
	'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
	'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
	'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
	'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
	'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
	'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
	'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
	'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
	'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
	'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
	'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
	'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
	'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
	'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
	'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
	'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',)
	for indro in passe :
	    curl = url+indro
	    try :
	        openurl = urllib.request.urlopen(curl)
	        print("_____________________________________________________________")
	        print("                                                             ")
	        print("\033[92m :::: Successful ::: ADMIN PAGE IS FOUND ::: "+curl)
	        print("_____________________________________________________________")
	    except urllib.error.URLError as msg :
	        print ("\033[91m =>>> SORRY NOT FOUND <<<= "+curl)
	

	print ("----------------------------------------------------------------------------------------")
	print ("\033[93m             I HOPE I HAVE HELPED YOU ^_^ , Love From R00t Dev1l ^_^            ")
	print ("----------------------------------------------------------------------------------------")
		

		
banner = (""" 
\033[1;31m_____________            \033[1;34m __________            ________
\033[1;31m___  __ )__(_)______ _   \033[1;34m ___  ____/____  ________  ___/
\033[1;31m__  __  |_  /__  __ `/   \033[1;34m__  __/  __  / / /  _ \  __ \ 
\033[1;31m_  /_/ /_  / _  /_/ /    \033[1;34m_  /___  _  /_/ //  __/ /_/ / 
\033[1;31m/_____/ /_/  _\__, /     \033[1;34m /_____/  _\__, / \___/\____/  
\033[1;31m             /____/      \033[1;34m          /____/              
\033[32m------------------------------------------------------ """)
mainmenu = ("""             =>>>Categories<<<=
------------------------------------------------------
\033[1;31m1.Link Grabber        |  \033[1;34m6.Website Whatweb
                      |
\033[1;34m2.DNS Map             |  \033[1;33m7.HTTP Header Grabber
                      |
\033[1;33m3.IP Scan             |  \033[32m8.DNS Recon 
                      |
\033[32m4.Who is Domain Scan  |  \033[1;31m9.ClickJacking Test
                      |
\033[1;31m5.Robot Txt Scan      |  \033[1;34m10.Website Admin Pannel

""")
print("""
\033[92m
+===============================================+
|..................Big Eye6.....................|
+-----------------------------------------------+
|#Created By =>>       R00t Dev1l               |
|#Date Created :     01 February 2021           |
|#Join=>> Gray Hat Hackers Community on Facebook|
|#mail=>>         indradas4863@gmail.com        |
|#Note=>>        Educational purpose only       |
+===============================================+ """)

time.sleep(1)
os.system("clear")

print("=>>>Please Login to continue<<<=")
print(" ")
username = input("Username:")
password = input("Password:")
if password == "We_@re_gr@y_h@T" and username == "GHHC":
	print(" ")	
	print("***Login Successfull***")
	print(" ")
	print(banner)
	print(mainmenu)

	choice = int(input("\033[1;37mPlease select a category==>"))

	if choice == 1:
		print(" ")
		linkrabber()
		print(linkgrabber())
	elif choice == 2:
		print(" ")
		dnsmap()
		print(dnsmap())
	elif choice == 3:
		print(" ")
		ipscan()
		print(ipscan())
	elif choice == 4:
		print (" ")
		whoisdomain()
		print(whoisdomain())
	elif choice == 5:
		print (" ")
		rbottxtscan()
		print(robottxtscan())
	elif choice == 6:
		print(" ")
		whatweb()
		print(whatweb())
	elif choice == 7:
		print(" ")
		httpheader()
		print(httpheader())
	elif choice == 8:
		print(" ")
		dnsrecon()
		print(dnsrecon())
	elif choice == 9:
		print(" ")
		clickjackingtest()
		print(clickjackingtest())
	elif choice == 10:
		print(" ")
		adminpanel()
		print(adminpanel())
	else:
		print(" ")
		print("       \033[91m Invalid Input") 

else:
    print("Incorrect Username or Password. Please try again.")


