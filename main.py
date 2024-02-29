# json.dumps(x)

import socket
import sys, time
import json
from socket import *
import multiprocessing
from colorama import *
from utils import *




smib_dict = {}

# class Smibs:
#     def __init__(self) -> None:
#         self.__smib_udp = {}
#     @property
#     def smib_udp(self):
#         return self.__smib_udp
#     @smib_udp.setter
#     def smib_udp(self, *args, **kwargs):

'''Create lists of machines with the same IP'''
def find_duplicate_ip(smib_dict:dict) -> dict:
    same_ip = {}
    n = len(smib_dict)
    if n < 2:
         return None
    for n in range(len(smib_dict)):
        
    while n > 0:
        
        k = 0
        while k < n:
            if smib_dict[n-1][0]['net_ip'] == smib_dict[k][0]['net_ip']:
                pass
            k += 1
        n -= 1
    return same_ip
        

'''Create lists of machines with the same MAC'''
# def find_duplicate_mac(smib_dict:dict) -> dict:


def main():

    while True:
        udp_broadcast(smib_dict)
        find_duplicate_ip(smib_dict)
        # find_duplicate_mac(smib_dict)


if __name__ == "__main__":
    start_time = time.time()
    main()

# search_proc = multiprocessing.Process(target=smib_search)
# search_proc.start()
# search_proc.join(2)
# if search_proc.is_alive():
#     search_proc.terminate() #search_proc.kill()
# search_proc.join()

# { "cmd": "setup", "cid0": 4522055, "cid1": 842158082, "cid2": 540030027, "name": "", "asset": 0, "flags": 0, "mac": "10:20:30:47:64:0E", "net_ip": "192.168.10.60", "net_mask": "255.255.255.0", "net_gw": "192.168.10.1", "udp_port": 30624, "tcp_port": 30625, "server_ip": "0.0.0.0", "server_port": 0, "sas_address": 1 }