<<<<<<< HEAD
=======
from urllib.request import urlopen
import json
import queue
import threading
import time

import parsers

# Produtor
def solicitacao_http():
	while not urls_para_baixar.empty():
		url = urls_para_baixar.get()
		paginas_para_analisar.put(urlopen(url).read())
		urls_para_baixar.task_done()

# Consumidor
def parse_html():
	while True:
		html = paginas_para_analisar.get()
		if html is None:
			break
		if not isinstance(html, str):
			html = str(html)
		parser = parsers.dados_perfil_uri()
		parser.feed(html)
		dados.append(parser.obter_dados_perfil())
		parser.close()
		paginas_para_analisar.task_done()
	
def preencher_fila_urls(arquivo):
	with open(arquivo) as url:
		for each in url:
			urls_para_baixar.put(each)

def iniciar_threads(numero, metodo, threads):
	for i in range(numero):
		thread = threading.Thread(target=metodo)
		thread.start()
		threads.append(thread)

urls_para_baixar, paginas_para_analisar = queue.Queue(), queue.Queue()
produtores, consumidores, dados = [], [], []
numero_produtores, numero_consumidores = 22, 1

# Preenche a fila com uma lista de URLs
preencher_fila_urls('URLs.txt')

# Marca o tempo inicial para analisar o desempenho
t0 = time.time()

# Inicia produtores
iniciar_threads(numero_produtores, solicitacao_http, produtores)

# Inicia consumidores
iniciar_threads(numero_consumidores, parse_html, consumidores)

# Aguarda todas as tarefas terminarem
urls_para_baixar.join()
paginas_para_analisar.join()

# Tempo de execução das tarefas
print(time.time() - t0)

# Para as threads
for i in range(numero_consumidores):
	paginas_para_analisar.put(None)

for thread in produtores:
	thread.join()

for thread in consumidores:
	thread.join()

with open(time.strftime('%d-%m-%Y-%H-%M') + '.json', 'w') as saida:
	for d in dados:
		json.dump(d, saida, indent=4)
>>>>>>> 7070949b5b854e7202dd488d65928c7c3f370b1b
