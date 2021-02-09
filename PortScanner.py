import socket
import pyfiglet
import threading
from queue import Queue


def scan_port(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip_domain, port))
        with print_lock:
            print(f'{port} is open')
        client.close()
    except socket.timeout:
        client.close()
    except socket.error:
        client.close()


def threader():
    while True:
        runner = queue.get()
        scan_port(runner)
        queue.task_done()


if __name__ == '__main__':
    banner = pyfiglet.figlet_format('PORT SCANNER')
    print(banner)

    socket.setdefaulttimeout(1)
    print_lock = threading.Lock()

    ip_domain = input('Enter please you host (example: google.com or 192.168.0.1): ')
    if ip_domain == '':
        print('You must specify a host!')
    port1 = int(input('Range port from: '))
    port2 = int(input('Range port before: '))
    queue = Queue()
    for x in range(100):
        thred = threading.Thread(target=threader, daemon=True)
        thred.start()
    try:  # translate hostname to IPv4
        host = socket.gethostbyname(ip_domain)
        print(f'Start scan on host {host}')
        for worker in range(port1, port2):
            queue.put(worker)
        queue.join()
        print(f'End scan host {host}')
    except ConnectionError:
        print('There was an error resolving the domain')
