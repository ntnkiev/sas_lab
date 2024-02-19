# json.dumps(x)

import socket
import sys, time
import json
from socket import *
import multiprocessing

UDP_IP = gethostbyname(gethostname())
UDP_PORT = 30624
TCP_PORT = 30625

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(2.0)

smib_dict = {}

def smib_search() -> dict:

    while True:
        command = '{"cmd":"browse"}'.encode()
        sock.sendto(command, ('<broadcast>', UDP_PORT))
        while True:
            try:
                data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                if data != command:
                    jsn = json.loads(data)
                    if addr not in smib_dict:
                        smib_dict.update({addr : jsn})
                    print (smib_dict)
                    time.sleep(5)
                    break
            except TimeoutError:
                print("UDP socket timeout error")
                break

if __name__ == "__main__":
    smib_search()
# search_proc = multiprocessing.Process(target=smib_search)
# search_proc.start()
# search_proc.join(2)
# if search_proc.is_alive():
#     search_proc.terminate() #search_proc.kill()
# search_proc.join()

# { "cmd": "setup", "cid0": 4522055, "cid1": 842158082, "cid2": 540030027, "name": "", "asset": 0, "flags": 0, "mac": "10:20:30:47:64:0E", "net_ip": "192.168.10.60", "net_mask": "255.255.255.0", "net_gw": "192.168.10.1", "udp_port": 30624, "tcp_port": 30625, "server_ip": "0.0.0.0", "server_port": 0, "sas_address": 1 }