import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_ip = input("Introduceți IP-ul serverului: ")
    client_socket.connect((server_ip, 5005))

    while True:
       
        message = input("Client (tu): ")
        client_socket.send(message.encode('utf-8'))
        
        if message.lower() == 'exit':
            break

        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("Serverul a închis conversația.")
            break
        print(f"Server: {data}")

    client_socket.close()
    print("Conexiune închisă.")

if __name__ == "__main__":
    start_client()