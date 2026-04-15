import socket
from termcolor import colored
# print(colored("Hello", "green"))

def scan(target, ports):
    print('\n'+'Starting Scan For: '+ str(target))
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+] Port Opened....' + str(port))
        sock.close()
    except:
        # print('[-] Port Closed..!!' + str(port))
        pass


targets = input("[*] Enter Targets to Scan(Split them by ,): ")
ports = int(input("[*] Enter How many Ports You want to Scan: "))

if ',' in targets:
    print(colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), ports)
else:
    scan(targets, ports)
