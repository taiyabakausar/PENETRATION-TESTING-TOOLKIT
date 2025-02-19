import socket

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)  # If the port is open, add it to the list
        sock.close()
    return open_ports