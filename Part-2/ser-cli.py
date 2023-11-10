import socket
import argparse
import time
import random
import string

def generate_random_string(length):
    return ''.join('abcdeqwjkdnkasdalskdjnslKAMSMAS'*length)

def server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)

    print(f"Server listening on port {port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

def client(server_ip, server_port, congestion_control):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set TCP congestion control algorithm
    client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_CONGESTION, congestion_control.encode())

    client_socket.connect((server_ip, server_port))

    print(f"Connected to server {server_ip}:{server_port} with congestion control {congestion_control}")

    while True:
        data_to_send = generate_random_string(10000)
        client_socket.sendall(data_to_send.encode())
        time.sleep(1)  # Adjust as needed

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP Client-Server Program')
    parser.add_argument('--role', choices=['server', 'client'], help='Specify the role (server/client)', required=True)
    parser.add_argument('--port', type=int, help='Port number', required=True)
    parser.add_argument('--config', choices=['b', 'c'], help='Configuration (b or c)', required=True)
    parser.add_argument('--congestion', choices=['vegas', 'reno', 'cubic', 'bbr'], help='Congestion control scheme', required=True)

    args = parser.parse_args()

    if args.role == 'server':
        server(args.port)
    elif args.role == 'client':
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(hostname, ip_address)
        if args.config == 'b' and ip_address == '10.0.0.1':
            client('10.0.0.4', args.port, args.congestion)
        elif args.config == 'c':
            client('10.0.0.4', args.port, args.congestion)