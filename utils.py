from socket import *
import json

UDP_IP = gethostbyname(gethostname())
UDP_PORT = 30624
TCP_PORT = 30625
cmd_setup = '{ "cmd": "setup", "cid0": 4522055, "cid1": 842158082, "cid2": 540030027, "name": "", "asset": 0, "flags": 0, "mac": "10:20:30:47:64:0E", "net_ip": "192.168.38.09", "net_mask": "255.255.255.0", "net_gw": "192.168.10.1", "udp_port": 30624, "tcp_port": 30625, "server_ip": "0.0.0.0", "server_port": 0, "sas_address": 1 }'

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(.5)

'''Create a list of all found slot machines'''
def udp_broadcast(smib_dict:dict) -> dict:
    command = '{"cmd":"browse"}'.encode()
    # print("Start broadcast")
    sock.sendto(command, ('<broadcast>', UDP_PORT))
    while True:
        try:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if addr != (UDP_IP, UDP_PORT):
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
