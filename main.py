# json.dumps(x)

import sys, time
import json
from socket import *
# import multiprocessing
from colorama import *
from utils import *

# class Smibs:
#     def __init__(self) -> None:
#         self.__smib_udp = {}
#     @property
#     def smib_udp(self):
#         return self.__smib_udp
#     @smib_udp.setter
#     def smib_udp(self, *args, **kwargs):


def main():
    smib_dict = {}

    while True:
        udp_broadcast(smib_dict)
        find_duplicate_field(smib_dict, 'net_ip')
        find_duplicate_field(smib_dict, 'mac')


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