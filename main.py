# json.dumps(x)

from collections import UserDict
import sys, time
import json
from socket import *

# import multiprocessing
from colorama import *
from utils import *

# from smib_command import *

tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.bind((HOST, TCP_PORT))
tcp_sock.settimeout(0.5)


class Smib:
    def __init__(self, id: dict) -> None:
        self.cid = str(id["cid0"]) + ":" + str(id["cid1"]) + ":" + str(id["cid2"])
        self.data = id
        self.socket = None

    @property
    def smib_udp(self):
        return self.__smib_udp

    @smib_udp.setter
    def smib_udp(self, *args, **kwargs):
        return self.__smib_udp


class Hall(UserDict):

    def add_slot(self, smib):
        self.data[smib.cid] = smib.data

        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((smib.data["net_ip"], TCP_PORT))
            self.data[smib.cid]["socket"] = sock

    def send_command(self, cid, command):
        self.data[cid]["socket"].sendall(command)
        data = self[cid].socket.recv(1024)
        return data

    def find_smib(self, cid):
        if cid in self.data.keys():
            return self.data[cid]
        else:
            return None


def main():
    hall = Hall()
    while True:
        smib_dict = {}
        udp_broadcast(smib_dict)
        same_ip = find_duplicate_field(smib_dict, "net_ip")
        if same_ip:
            for key, value in same_ip.items():
                print(f"{Fore.RED}Boards {value} have same ip {key}{Style.RESET_ALL}")
        same_mac = find_duplicate_field(smib_dict, "mac")
        if same_mac:
            for key, value in same_mac.items():
                print(f"Boards {value} have same mac {key}")
        for cid, data in smib_dict.items():
            if cid == "2031659:1111642132:540095031":
                pass
            elif not hall.find_smib(cid):
                smib = Smib(data)
                hall.add_slot(smib)
            else:
                print(hall.send_command(cid, command(cmd_identify, data)))


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
