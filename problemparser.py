from urllib.request import urlopen
import csv
import queue
import re
import threading

from bs4 import BeautifulSoup


# conta quantas páginas de problemas resolvidos um perfil possui.
def n_of_pages(page):
    content = page.div.find(id='table-info').contents[0]  # i.e "1 of 32"
    return [int(i) for i in content.split() if i.isdigit()][-1]


# extrai o id do problema e o seu url.
def problem_row_data(tr):
    for td in tr.find_all('td'):
        if td.a:
            return td.a.contents[0], td.a.get('href')


# extrai quando um problema foi resolvido.
def solved_date(tr):
    for td in tr.find_all('td'):
        if not td.a:
            s = re.search('[0-9]+/[0-9]+/[0-9]+', ''.join(td.contents))
            if s:
                return s.group(0)


# extrai a categoria de um problema e seu level.
def find_problem_info(url):
    problem_url = 'https://www.urionlinejudge.com.br' + url
    page = BeautifulSoup(urlopen(problem_url), 'html.parser')
    category = page.select('a.place-view')[0].contents[0]
    level = re.findall('\d+', page.h3.get('class')[0])[0]
    return category, int(level)


# extrai informações dos problemas resolvidos de uma página.
def scraper(url, data):
    page = BeautifulSoup(urlopen(url), 'html.parser')
    for tr in page.tbody.find_all('tr'):
        problem_id, problem_url = problem_row_data(tr)
        date = solved_date(tr)
        category, level = find_problem_info(problem_url)
        print(date, problem_id, category, level)
        data.put((date, problem_id, category, level))


# TODO: colocar um try...except quando ele faz um urlopen; colocar label no csv, para torna-lo mais flexivel
def problemparser(profile_id):
    profile_url = 'https://www.urionlinejudge.com.br/judge/pt/profile/%s' % profile_id
    page_url_base = 'https://www.urionlinejudge.com.br/judge/pt/profile/%s?page=' % profile_id
    soup = BeautifulSoup(urlopen(profile_url), 'html.parser')
    threads = []
    sync_data = queue.Queue()

    # para cada página cria uma thread que irá extrair informações sobre os
    # problemas resolvidos.
    for page in range(1, n_of_pages(soup) + 1):
        page_url = page_url_base + str(page)
        thread = threading.Thread(target=scraper, args=(page_url, sync_data))
        thread.start()
        threads.append(thread)

    # espera todas as threads terminarem suas tarefas.
    for thread in threads:
        thread.join()

    data = []

    # extrai as informações da fila.
    while not sync_data.empty():
        data.append(sync_data.get())

    # extrai o id do perfil, com base na url de entrada.
    profile_id = profile_url.rsplit('/', 1)[-1]

    # ordena pela data que o problema foi resolvido.
    sdata = sorted(data, key=lambda d: list(map(int, d[0].split('/')[::-1])))

    # salvas as informações de cada problema em uma arquivo csv.
    with open(profile_id + '.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile)
        for row in sdata:
            writer.writerow(row)


if __name__ == '__main__':
    problemparser(20268)
