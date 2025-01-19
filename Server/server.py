import socket
import threading
import queue
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import json

# Клиент-серверное приложение для обкачки набора урлов с ограничением нагрузки
# Cервер
# master-worker cервер для обработки запросов от клиента.

# Алгоритм должен быть следующим:

# - Сервер должен поддерживать взаимодействие с любым числом клиентов;
# - Мастер и воркеры это разные потоки в едином приложении сервера;
# - Количество воркеров задается при запуске;
# - Мастер слушает порт, на который клиенты будут по TCP отправлять урлы для обкачки;
# - Мастер принимает запроc и передает его одному из воркеров;
# - Воркер читает url от клиента;
# - Воркер обкачивает url по http и возвращает клиенту топ K самых частых слов и их частоту в формате json {"word1": 10, "word2": 5};
# - После каждого обработанного урла сервер должен вывести статистику: сколько урлов было обработано на данный момент суммарно всеми воркерами;
# python server.py -w 10 -k 7 (сервер использует 10 воркеров для обкачки и отправляет клиенту топ-7 частых слов)

# Все действия должны быть выделены в классы/функции.

# Клиент
# Утилита, отправляющая запросы с урлами серверу по TCP в несколько потоков. Нужно сделать следующее:

# - Подготовить файл с запросами (порядка 100 разных url);
# - На вход клиенту передаётся два аргумента --- файл с URL'ами и количество потоков M;
# - Клиент создает M потоков, отправляет запросы на сервер в каждом потоке и печатает ответ сервера в стандартый вывод, например: `xxx.com: {'word1': 100, 'word2': 50}`.
# python client.py 10 urls.txt

# Все действия должны быть выделены в классы/функции.

class Server:
    def __init__(self, worker, k):
        self.w = worker
        self.k = k
        self.host = '127.0.0.1'
        self.port = 65000
        self.url_count = 0
        self.lock = threading.Lock()  

    def master(self):
        que = queue.Queue()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Сервер запущен на {self.host}:{self.port}")

            workers = [
                threading.Thread(
                    target=self.worker,
                    args=(que,)
                )
                for _ in range(self.w)
            ]

            for worker in workers:
                worker.start()

            while True:
                client_socket = server_socket.accept()[0]
                data = client_socket.recv(1024)
                url = data.decode()
                if url:
                    que.put((client_socket, url))
                else:
                    client_socket.close()

    def worker(self, que):
        while True:
            client_socket, url = que.get()
            if url is None:
                que.put(url)
                break

            try:
                response = requests.get(url)
                response.raise_for_status() 

                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()

                words = re.findall(r'\w+', text.lower())
                counter = Counter(words).most_common(self.k)
                result = json.dumps(dict(counter))

                client_socket.sendall(result.encode())
            except Exception as e:
                print(f"Ошибка обработки URL {url}: {e}")
                client_socket.sendall(f"Ошибка обработки URL: {url}".encode())
            finally:
                client_socket.close()

            with self.lock:
                self.url_count += 1
                print(f"Обработано URL: {self.url_count}")

    def run(self):
        master_thread = threading.Thread(
            target=self.master
        )
        master_thread.start()
