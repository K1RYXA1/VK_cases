import argparse
import asyncio
from collections import Counter
import json
import re

import aiofiles
import aiohttp
from bs4 import BeautifulSoup

async def fetch_url(url, session):
    async with session.get(url) as resp:
        text = await resp.text()
        result = await asyncio.to_thread(process_text, text)
        return result

def process_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\w+', text.lower(), flags=re.ASCII)
    counter = Counter(words).most_common(5)
    return json.dumps(dict(counter))

async def reader(urls, que):
    async with aiofiles.open(urls, mode='r', encoding='utf-8') as f:
        async for url in f:
            await que.put(url.strip('\n'))

async def fetch_worker(que, session, sem):
    while True:
        url = await que.get()
        try:
            async with sem:
                result = await fetch_url(url, session)
                print(result)
        except Exception as err:
            print(err)
            raise err
        finally:
            que.task_done()

async def fetch_batch_urls(urls, n):
    que = asyncio.Queue()
    sem = asyncio.Semaphore(n)
    workers = []
    async with aiohttp.ClientSession() as session:
        read_url = asyncio.create_task(reader(urls, que))
        for _ in range(n):
            workers.append(asyncio.create_task(fetch_worker(que, session, sem)))
        await read_url
#         await read_url

        await que.join()
#         await que.join()

        for wrk in workers:
            wrk.cancel()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int, help='Количество одновременных запросов.')
    parser.add_argument('urls', type=str, help='Файл с URL-адресами.')
    args = parser.parse_args()
    asyncio.run(fetch_batch_urls(args.urls, args.c))
