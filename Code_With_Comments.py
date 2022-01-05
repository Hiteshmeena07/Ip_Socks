# -*- coding: utf-8 -*-

import time     #time module allows to work with time in Python. It allows functionality like getting the current time, pausing the Program from executing, etc.

import os      # The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.

import subprocess   #Subprocess module used to run new codes and applications by creating new processes. It lets you start new applications right from the Python program you are currently writing. So, if you want to run external programs from a git repository or codes from C or C++ programs, you can use subprocess




try:                                                                               #try Command to check conditon
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)     #check for python3 available/Upgrade
    if str('install ok installed') in str(check_pip3):                          #tells that its installed or you want to install
        pass                                                              #if we select install it passes the command to except
except subprocess.CalledProcessError:                                       
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)   #to install the latest versions of the packages currently installed on the user's system 
    
    
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)      #Install python3
    print('[!] pip3 installed succesfully')                                     #Python3 installed sucessfully



try:                                                                             #try Command to check condition

    import requests                                                # requests module allows you to send HTTP requests using Python.
except Exception:                    #exception handling code If the above import requests gives error this Code of block will run
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')   # Install Requests[socks] that uses Socks with requests
    print('[!] python3 requests is installed ')
try:                                                              #try Command to check condition
    check_tor = subprocess.check_output('which tor', shell=True)    # Check the present version of Tor
except subprocess.CalledProcessError:                # if the tor is not available then Below block of code will run

    print('[+] tor is not installed !')                     
    subprocess.check_output('sudo apt update',shell=True) #to install the latest versions of the packages currently installed on the user's system 
    
    subprocess.check_output('sudo apt install tor -y',shell=True)  #Tor will install on system
    print('[!] tor is installed succesfully ')

os.system("clear")                 #Clear the Shell
def ma_ip():
    url='https://www.myexternalip.com/raw'            #Checks the Current Ip of System Network
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')) #Redirect Network THrough Ip_Socks 
    
    return get_ip.text

def change():
    os.system("service tor reload")                                   #Request Tor to Mask Given IP for New Ip
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))         #Print The New Changed Ip 

print('''\033[1;32;40m \n
                                                        
 mmmmm                 mmmm                #            
   #    mmmm          #"   "  mmm    mmm   #   m   mmm  
   #    #" "#         "#mmm  #" "#  #"  "  # m"   #   " 
   #    #   #             "# #   #  #      #"#     """m 
 mm#mm  ##m#"         "mmm#" "#m#"  "#mm"  #  "m  "mmm" 
        #                                               
        "                                               
Created By:-Netaji Subhas University Technology (West Campus)
Members:- Hitesh:::Jaisal:::Mayank
''')
print("\033[1;40;31m https://github.com/Hiteshmeena07/\n")          #Source Code Link

os.system("service tor start")                                      #Start the Tor Server




time.sleep(3)                                                            # suspends execution for the given number of seconds
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")          #Modify your Browser Settings Accordingly
os.system("service tor start")                                           #Start the Tor Server
x = input("[+] time to change Ip in Sec [type=60] >> ")                  #Insert the time to change Ip in Sec
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>") #No. of times Ip to be Changed For Infinte Loop Insert 0 Sec.


if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()                                        #Ip Will Change Till the given Time
		except KeyboardInterrupt:

		 	print('\nauto tor is closed ')                  # When the program will Close The Message will be Display.
		 	quit()                                          # Quit the Program

else:
	for i in range(int(lin)):
		    time.sleep(int(x))                                       # Same as above and the loop will Go onn
		    change()
