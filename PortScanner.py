import socket
import pyfiglet
import sys
import threading
from queue import Queue

socket.setdefaulttimeout(1)
print_lock = threading.Lock()

banner = pyfiglet.figlet_format('PORT SCANNER')
print(banner)

ip_domain = input('Enter please you host (example: google.com or 192.168.0.1): ')
if ip_domain == '':
    print('You must specify a host!')
else:
    pass

port1 = int(input('Range port from: '))
port2 = int(input('Range port before: '))


def scan_port(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip_domain, port))
        with print_lock:
            print(port, 'is open')
        client.close()
    except Exception:
        pass


def threader():
    while True:
        worker = q.get()
        scan_port(worker)
        q.task_done()


q = Queue()

for x in range(100):
    thred = threading.Thread(target=threader, daemon=True)
    thred.start()


try:  # translate hostname to IPv4
    host = socket.gethostbyname(ip_domain)
    print(f'Start scan on host {host}')
    for worker in range(port1, port2):
        q.put(worker)
    q.join()
    print(f'End scan host {host}')
except ConnectionError:
    print('There was an error resolving the domain')
    sys.exit()
except socket.error:
    print('Server not responding!')
    sys.exit()