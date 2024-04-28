import socket

target_host = input("Enter the target hostname or IP address: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"Scanning ports on {target_host}...")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port}: Open")
    sock.close()
