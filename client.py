import socket

def start_client():
    # Crearea socket-ului TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectarea la server (folosiți IP-ul colegului din ZeroTier) [cite: 14]
    server_ip = input("Introduceți IP-ul serverului: ")
    client_socket.connect((server_ip, 5005))

    while True:
        # 1. Clientul trimite primul mesaj 
        message = input("Client (tu): ")
        client_socket.send(message.encode('utf-8'))
        
        if message.lower() == 'exit':
            break

        # 2. Așteptare răspuns de la server
        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("Serverul a închis conversația.")
            break
        print(f"Server: {data}")

    # Închidere grațioasă 
    client_socket.close()
    print("Conexiune închisă.")

if __name__ == "__main__":
    start_client()