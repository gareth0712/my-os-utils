import socket
import termcolor
import re

def scan(targets, ports):
  if any(pattern in targets for pattern in (',', ', ', ' ,')):
    print(termcolor.colored('[*] Scanning multiple targets', 'green'))
  else:
    print(f'[*] Scanning target: {targets}')
  for ip_addr in re.split(',|, | ,', targets):
    scan_port(ip_addr.strip(), ports)

def scan_port(ipaddress, ports):
  print(f'\n[*] Starting scan for {ipaddress}')
  for port in range(1, int(ports)):
    try:
      sock = socket.socket()
      sock.connect((ipaddress, port))
      print(f'[+] Port Opened {str(port)}')
      sock.close()
    except:
      pass

targets = input('[*] Enter targets to scan(split them by ,): ')
ports = input('[*] Enter number of ports to scan: ')

scan(targets, ports)
