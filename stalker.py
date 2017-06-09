from urllib.request import urlopen
import json
import queue
import threading
import time

import parsers

# Producers
def http_request():
	while not url_to_request.empty():
		url = url_to_request.get()
		html_to_parse.put(urlopen(url).read())
		url_to_request.task_done()

# Consumer
def parse_html():
	while True:
		html = html_to_parse.get()
		if html is None:
			break
		if not isinstance(html, str):
			html = str(html)
		parser = parsers.uri_profile_information()
		parser.feed(html)
		data.append(parser.get_profile_data())
		parser.close()
		html_to_parse.task_done()
	
def fill_url_request(filename):
	with open(filename) as url:
		for each in url:
			url_to_request.put(each)

def start_threads(number, target, pool):
	for i in range(number):
		thread = threading.Thread(target=target)
		thread.start()
		pool.append(thread)

url_to_request, html_to_parse = queue.Queue(), queue.Queue()
pthreads, cthreads, data = [], [], []
n_producers, n_consumers = 22, 1

# fill the queue with a list of url
fill_url_request('url_list.txt')

# get time to measure performance
t0 = time.time()

# start producers
start_threads(n_producers, http_request, pthreads)

# start consumers
start_threads(n_consumers, parse_html, cthreads)

# block until all task are done
url_to_request.join()
html_to_parse.join()

# time necessary to perform all tasks
print(time.time() - t0)

# stop threads
for i in range(n_consumers):
	html_to_parse.put(None)

for thread in pthreads:
	thread.join()

for thread in cthreads:
	thread.join()
	
print(data)

with open(time.strftime('%d-%m-%Y-%H-%M') + '.json', 'w') as out:
	for d in data:
		json.dump(d, out, indent=4)
'''
Statistic:

(P, C, T) -> Number of Producers, Consumers and Tasks

( 1,  1, 22) = 72s~
( 5, 11, 22) = 18s~
(11,  1, 22) = 15s~
(22,  1, 22) = 7s~
(22, 11, 22) = 7s~
''' 
