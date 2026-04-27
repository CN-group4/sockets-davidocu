import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 5006))
    
    print("Serverul UDP este pornit și așteaptă mesaje...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        
        if not message or message.lower() == 'exit': 
            print(f"Comunicare închisă de {client_address}")
            break
            
        print(f"Client ({client_address}): {message}")

        reply = input("Server: ")
        server_socket.sendto(reply.encode('utf-8'), client_address)
        
        if reply.lower() == 'exit':
            break

    server_socket.close()
    print("Server oprit.")

if __name__ == "__main__":
    start_udp_server()