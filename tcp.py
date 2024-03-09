from socket import *

HOST = gethostbyname(gethostname())
UDP_PORT = 30624
TCP_PORT = 30625


def create_tcp_socket():
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.bind((HOST, TCP_PORT))
    tcp_sock.settimeout(0.5)

    with tcp_sock:
        tcp_sock.connect(("192.168.38.56", TCP_PORT))
        tcp_sock.sendall('{ "cmd": "identify", "cid0": 4718662, "cid1": 842158089, "cid2": 540030027}'.encode())
        # tcp_sock.sendall('{"cmd":"browse"}'.encode())
        data = tcp_sock.recv(1024)

    print(f"Received {data!r}")

create_tcp_socket()