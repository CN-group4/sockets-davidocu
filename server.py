import socket


def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    bind_ip = input("Introduceți IP-ul pe care ascultă serverul (ex: 0.0.0.0): ")
    server_socket.bind((bind_ip, 5005))
    server_socket.listen(1)
    print(f"Server pornit pe {bind_ip}:5005. Așteaptă conexiune...")

    conn, addr = server_socket.accept()
    print(f"Client conectat: {addr[0]}:{addr[1]}")

    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data or data.lower() == "exit":
                print("Clientul a închis conversația.")
                break
            print(f"Client: {data}")

            message = input("Server (tu): ")
            conn.send(message.encode("utf-8"))
            if message.lower() == "exit":
                break
    finally:
        conn.close()
        server_socket.close()
        print("Conexiune închisă.")


if __name__ == "__main__":
    start_server()
