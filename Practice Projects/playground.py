import socket 
import termcolor

def scan(target, ports):
    print('\n'+'Starting Scan for: '+ str(target))
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored(('[+] Port Open..'), 'light_green') + str(port))
        sock.close()
    except:
        # print(termcolor.colored(('[-] Port Closed..'),'red')+ str(port))
        pass

targets = input('[*] Enter Targets to Scan(split them by ,): ')
ports = int(input('[*] Enter How many Ports you want to Scan: '))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'light_blue'))
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), ports)
else:
    scan(targets, ports)