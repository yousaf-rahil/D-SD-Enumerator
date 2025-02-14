import os               #for a clear terminal
os.system('cls' if os.name == 'nt' else 'clear')   
from tqdm import tqdm   #to create the loading bar
import dns.resolver     #for doing dns enumaration
import time             #help with time managment in program
import socket           #to check if the device is connected to the internet
import sys              #to quite the program in case of connection lose



#checking connection
def connection():
    socket.create_connection(('8.8.8.8', 53), timeout=5)
    return True

if not connection():
    print("No Internet! Please connect to the internet to use the program")
    sys.exit(1)

else:
    print("Program Started!")
    #loading bar
    def starter(item):
        time.sleep(0.009)

    for item in tqdm(range(100), desc="Loading"):
        starter(item)

    #main DNS Enumorator
    target_domain = "youtube.com"      #Change this to change the target
    record_list = ['A', 'AAAA', 'CNAME', 'MX', 'TXT']   #DNS record list

    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8'] #google public DNS

    for i in record_list:
        try:
            answer = resolver.resolve(target_domain, i)
            if answer.rrset:        #rrset is to check if all the data was retrived
                print(f"{i} records of {target_domain}")
                for data in answer.rrset:
                    print(f"\t{data}")
        except dns.resolver.NoAnswer:
            continue
    print("PROGRAM FINSIHED...\n\n")
