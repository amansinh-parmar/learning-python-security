import socket
import termcolor

def scan(targets, ports):
    print('\n'+'Starting Scan For: '+ str(targets))
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        socket = socket.socket()
        socket.connect((ipaddress, port))
        print('[+] Port Opened....' + str(port))
        socket.close()
    except:
        print('[-] Port Closed..!!' + str(port))


targets = input("[*] Enter Targets to Scan(Split them by ,): ")
ports = int(input("[*] Enter How many Ports You want to Scan: "))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), ports)
else:
    scan(targets, ports)
