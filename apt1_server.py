import socket
s = socket.socket()
s.bind(("0.0.0.0", 80))
s.listen()
client_socket, address = s.accept()
print(f"[+] {address} is connected.")
with open("received_file.zip", "wb") as f:
    while True:
        bytes_read = client_socket.recv(4096)
        if not bytes_read:
            break
        f.write(bytes_read)
client_socket.close()
s.close()