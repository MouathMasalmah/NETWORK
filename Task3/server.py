from socket import *

def open_file(file_name):
    try:
        with open(file_name, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None

serverPort = 1833
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    try:
        sentence = connectionSocket.recv(1024).decode()
        print('Received: ', sentence)
        split = sentence.split(" ")
        s = split[1].split("/")
        file = s[1]

        if (sentence.startswith("GET / ") or file == "en" or file == "main_en.html" or file == "index.html"):
            content = open_file('main_en.html')
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file == "ar" or file == "main_ar.html":
            content = open_file('main_ar.html')
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file.endswith(".css"):
            content = open_file(file)
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: text/css\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file.endswith(".html"):
            content = open_file(file)
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif "get_image?image-in" in file:
            name = sentence.split("=")[1].split(" ")[0]
            content = open_file(name)
            if content:
                if name.endswith(".jpg"):
                    connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: image/jpg\n\n')
                elif name.endswith(".png"):
                    connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: image/png\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file.endswith(".jpg"):
            content = open_file(file)
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: image/jpg\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file.endswith(".png"):
            content = open_file(file)
            if content:
                connectionSocket.send(b'HTTP/1.1 200 OK\nContent-Type: image/png\n\n')
                connectionSocket.send(content)
            else:
                raise FileNotFoundError

        elif file == "so":
            connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\nContent-Type: text/html; charset=utf-8\r\nLocation: https://stackoverflow.com\r\n\r\n")

        elif file == "itc":
            connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\nContent-Type: text/html; charset=utf-8\r\nLocation: https://itc.birzeit.edu/\r\n\r\n")

        else:
            raise FileNotFoundError

    except Exception as e:
        print(f"Error: {e}")
        connectionSocket.send(b'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n')
        error_content = open_file('error.html')
        if error_content:
            connectionSocket.send(error_content + f"<p> ip: {ip} port: {port} </p>".encode())
        else:
            connectionSocket.send(b'<html><body><h1>404 Not Found</h1><p>File not found.</p></body></html>')
    finally:
        connectionSocket.close()
