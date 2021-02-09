import socket


def scan_port(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if client.connect_ex((host, port)):
        print(f"Port {port} close")
    else:
        print(f"Port {port} open")


ip_domain = input('Enter plase you domain(example: google.com): ')
if ip_domain == '':
    print('You must specify a host!')

port1 = int(input('Range port from: ')) 
port2 = int(input('Range port before: '))

try:
    host = socket.gethostbyname(ip_domain)
    for i in range(port1, port2 + 1):
        scan_port(host, i)
except ConnectionError:
    print('There was an error resolving the domain')
