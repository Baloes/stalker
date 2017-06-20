from bs4 import BeautifulSoup
from urllib.request import urlopen

import threading
import queue
import time
import os

def save(url, html):
	path = 'URI/' + url.strip('http://').replace('/', '.')
	with open(path + '.html', 'w+') as f:
		f.write(html.decode())

def download():
	while True:
		url = url_queue.get()
		print('GET', url)
		html = urlopen(url).read()
		save(url, html)
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.find_all('a'):
			if all(p not in link.get('href') for p in ['#', 'http']):
				to_fetch = root + link.get('href')
				if to_fetch not in opened:
					url_queue.put(root + link.get('href'))
					opened.add(to_fetch)
		url_queue.task_done()
		
root = 'http://urionlinejudge.com.br'
url_queue = queue.Queue()
url_queue.put(root)
opened = {root}
threads = []
n_threads = 30

t0 = time.time()

for i in range(n_threads):
	thread = threading.Thread(target=download)
	thread.start()
	threads.append(thread)

url_queue.join()

for i in range(n_threads):
	url_queue.put(None)
	
for thread in threads:
	thread.join()

print('TAKE', time.time() - t0, 'TO OPEN')	
print(opened)

