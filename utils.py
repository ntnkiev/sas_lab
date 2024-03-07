from socket import *
import json
from time import sleep

HOST = gethostbyname(gethostname())
UDP_PORT = 30624
TCP_PORT = 30625
cmd_setup = '{ "cmd": "setup", "cid0": 4522055, "cid1": 842158082, "cid2": 540030027, "name": "", "asset": 0, "flags": 0, "mac": "10:20:30:47:64:0E", "net_ip": "192.168.38.09", "net_mask": "255.255.255.0", "net_gw": "192.168.10.1", "udp_port": 30624, "tcp_port": 30625, "server_ip": "0.0.0.0", "server_port": 0, "sas_address": 1 }'
#{ "cmd": "setup", "cid0": 4718662, "cid1": 842158089, "cid2": 540030027, "name": "", "asset": 0, "flags": 0, "mac": "10:20:30:4A:64:04", "net_ip": "192.168.38.56", "net_mask": "255.255.255.0", "net_gw": "192.168.38.1", "udp_port": 30624, "tcp_port": 30625, "server_ip": "0.0.0.0", "server_port": 0, "sas_address": 1 }
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((HOST, UDP_PORT))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(.5)

'''Create a list of all found slot machines'''
def udp_broadcast(smib_dict:dict) -> dict:
    command = '{"cmd":"browse"}'.encode()
    print("Start broadcast")
    sock.sendto(command, ('<broadcast>', UDP_PORT))
    while True:
        try:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if addr != (HOST, UDP_PORT):
                jsn = json.loads(data)
                cid = None
                try:
                    cid = str(jsn['cid0']) + str(jsn['cid1']) + str(jsn['cid2'])
                except KeyError:
                    pass
                if cid and (cid not in smib_dict):
                    smib_dict.update({cid : jsn})

        except TimeoutError:
            return smib_dict
        
# def tcp_con(serv_ip, command) -> dict:
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((serv_ip, TCP_PORT))
#         s.sendall(b"Hello, world")
#         data = s.recv(1024)
#         jsn = json.loads(data)
#         print(jsn)

        
'''Create dict of machines with the same fields value'''
def find_duplicate_field(smib_dict: dict, field: str) -> dict:
    smibs = smib_dict.copy()
    same_field = {}
    if len(smibs) < 2:
         return same_field
    for item1 in smibs.items():
        current_cid = item1[0]
        current_item = smibs.pop(current_cid)
        for item2 in smibs.items():
            second_cid = item2[0]
            if current_item[field] == item2[1][field]:
                if current_item[field] in same_field:
                    same_field[current_item[field]].append(second_cid)
                else: same_field.update({current_item[field]: [current_cid, second_cid]})
        return same_field


def main():
    smib_dict = {}
    while True:
        print(udp_broadcast(smib_dict))
        sleep(5)
    # tcp_con()



if __name__ == "__main__":
    main()
