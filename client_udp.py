import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_ip = input("Introduceti IP-ul serverului (ZeroTier): ")
    server_address = (server_ip, 5006)

    while True:
        message = input("Client: ")
        client_socket.sendto(message.encode('utf-8'), server_address)
        
        if message.lower() == 'exit': 
            break

        data, _ = client_socket.recvfrom(1024)
        reply = data.decode('utf-8')
        
        if reply.lower() == 'exit':
            print("Serverul a inchis conversatia.")
            break
            
        print(f"Server: {reply}")

    client_socket.close()
    print("Client oprit.")

if __name__ == "__main__":
    start_udp_client()