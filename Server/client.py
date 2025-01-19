import socket
import threading
import queue
import argparse

class Client:
    def init(self, urls='urls.txt', M=1):
        self.M = M
        self.urls = urls  
        self.host = '127.0.0.1'  
        self.port = 65000  
        self.que = queue.Queue()  

    def connect_with_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            while True:
                url = self.que.get() 
                if url is None:
                    break
                client_socket.sendall(url.encode())
                response = client_socket.recv(1024)  
                print(response.decode('utf-8'))  

    def run(self):
        with open(self.urls, 'r', encoding='utf-8') as f:
            URLS = f.readlines()
            for url in URLS:
                self.que.put(url.strip())
            for _ in range(self.M):
                self.que.put(None)

        # Создание и запуск потоков
        threads = [
            threading.Thread(
                target=self.connect_with_server
            )
            for _ in range(self.M)
        ]

        for th in threads:
            th.start()  

        for th in threads:
            th.join()  

if __name__ == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument('num_threads', type=int, help='Количество потоков для отправки запросов.')
    parser.add_argument('urls_file', type=str, help='Путь к файлу с URL-адресами.')

    args = parser.parse_args()  

    client = Client(urls=args.urls_file, M=args.num_threads)
    client.run()  
