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
		from Files import LinkGrabber
		print(LinkGrabber)
	elif choice == 2:
		print(" ")
		from Files import dnsmap
		print(dnsmap)
	elif choice == 3:
		print(" ")
		from Files import ipscan
		print(ipscan)
	elif choice == 4:
		print (" ")
		from Files import WhoIsDomain
		print(WhoIsDomain)
	elif choice == 5:
		print (" ")
		from Files import RobotTXTSCAN
		print(RobotTXTSCAN)
	elif choice == 6:
		print(" ")
		from Files import whatweb
		print(whatweb)
	elif choice == 7:
		print(" ")
		from Files import HTTPHeaderGrabber
		print(HTTPHeaderGrabber)
	elif choice == 8:
		print(" ")
		from Files import dnsreconandsrv
		print(dnsreconandsrv)
	elif choice == 9:
		print(" ")
		from Files import ClickjackingTest
		print(ClickjackingTest)
	elif choice == 10:
		print(" ")
		from Files import adminpanel
		print(adminpanel)
	else:
		print(" ")
		print("       \033[91m Invalid Input") 

else:
    print("Incorrect Username or Password. Please try again.")


