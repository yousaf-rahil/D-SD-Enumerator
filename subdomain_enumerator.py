import os
os.system('cls' if os.name == 'nt' else 'clear') 
import socket                                    #impoorting sockets to check internet connection before the program starts
import sys                                       #to terminate the program in case of no internet    
import requests
import threading
#checking internet connection
def connection_check():
    socket.create_connection(("8.8.8.8", 53), timeout=5)
    return True
if not connection_check():
    print("Please connect to the internet to use the program...")
    sys.exit(1)
else:
#main body of program
    target = "youtube.com"

    with open("subdomains.txt") as file:            #opening a dictionary in which a list of subdomains is written
        subdomains = file.read().splitlines()       #creating a variable and storing the data in it. splitlines function converts the whole data as a list

    discovered_subdomains= []                       #empty list where we will store discovered sub-domains later on

    lock = threading.Lock()                         #making an object. "REMEMBER! Threading is a module and lock is a class"

    def sub_domain(subdomains):                     #here we are sending the whole list to the funciton. And the function will read it(items of list) one by one
        url = f"http://{subdomains}.{target}"       #making a variable "url" by combining subdomain and domain
        try:                                        #try and except function for error handling
            requests.get(url)                       #it will send a request to the url we have found out (ping the url)
        except requests.ConnectionError:            #in case there is an error, it will pass to next one
            pass
        except requests.Timeout:
            pass
        except KeyboardInterrupt:
            print("\n[!] Detected Ctrl + C. Exiting gracefully...")
            sys.exit(0)
        else:                                       #if there is no error,, it will print and write url in a file and consle
            print(f"[+] discovered a domain: {url}")
            with lock: 
                with open('discovered_subdomains.txt', 'a') as file:  # 'a' mode appends instead of overwriting
                    file.write(url + '\n')                             #using lock funciton to prevent writing multiple threads simultaneously
               # discovered_subdomains.append(url)

    thread = []                                     #empty list to store threads later
    for subdomain in subdomains:                    
        t1 = threading.Thread(target=sub_domain, args=(subdomain,))
        t1.start()
        thread.append(t1)
    for t1 in thread:
         t1.join()
with open("discovered_subdomains.txt", 'a') as file:
    file.write("\n\nThat's All...\n\n")
    
