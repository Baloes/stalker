from datetime import date
import csv
import math

import matplotlib.pyplot as plt


# carrega os dados de algum perfil da saída gerada pelo problemparser.
def load_data(profile_id):
    with open(profile_id + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# calcula a diferença, em dias, de duas datas.
def date_distance(d, d0):
    dd0, mm0, yy0 = map(int, d0.split('/'))
    dd, mm, yy = map(int, d.split('/'))
    return (date(yy, mm, dd) - date(yy0, mm0, dd0)).days


# calcula a pontuação de algum perfil, retornando uma lista de tuplas
# com o dia e a pontuação associada a esse dia.
def score(data, last_day=None):
    value = 0
    actual_date = data[0][0]
    for problem in data:
        if last_day and date_distance(problem[0], data[0][0]) > last_day:
            break
        if actual_date != problem[0]:
            actual_date = problem[0]
            yield date_distance(actual_date, data[0][0]), value
        value += int(problem[-1]) ** math.e


# calcula quantos problemas foram resolvidos em uma determinada categoria,
# retornando uma lista d e tuplas com o dia e a quantidade de cada categoria.
def category_solved(profile_id, last_day=None):
    category = {
        'Iniciante': 0, 'Ad-Hoc': 0,
        'Strings': 0, 'Estruturas e Bibliotecas': 0,
        'Matemática': 0, 'Paradigmas': 0,
        'Grafos': 0, 'Geometria Computacional': 0
    }
    data = load_data(profile_id)
    actual_date = data[0][0]
    for problem in data:
        if last_day and date_distance(problem[0], data[0][0]) > last_day:
            break
        if actual_date != problem[0]:
            actual_date = problem[0]
            yield date_distance(actual_date, data[0][0]), \
                  category['Iniciante'], category['Ad-Hoc'], \
                  category['Strings'], category['Estruturas e Bibliotecas'], \
                  category['Matemática'], category['Paradigmas'], \
                  category['Grafos'], category['Geometria Computacional']
        category[problem[2]] += 1


# mostra uma gráfico que indica a pontuação de um perfil, desde
# que sua conta foi criada.
def show_score_over_time(profiles_ids):
    for profile_id in profiles_ids:
        data = load_data(profile_id)
        x, y = zip(*score(data))
        plt.plot(x, y, label=profile_id)
    plt.title('Score')
    plt.xlabel('Day')
    plt.ylabel('Score')
    plt.legend()
    plt.show()


# mostra um gráfico que indica quantos problemas foram resolvidos
# em uma determinada categoria, desde que sua conta foi criada.
def show_problem_solved_by_category(profiles_ids, categories=None):
    categories_names = [
        'Iniciante', 'Ad-Hoc', 'Strings', 'Estruturas e Bibliotecas',
        'Matemática', 'Paradigmas', 'Grafos', 'Geometrica Computacional'
    ]
    if not categories:
        categories = categories_names
    for profile_id in profiles_ids:
        x, *category = zip(*category_solved(profile_id))
        for label, y in zip(categories_names, category):
            if label in categories:
                plt.plot(x, y, label='%s (%s)' % (label, profile_id))
    plt.title('Number of Problem Solved')
    plt.xlabel('Day')
    plt.ylabel('Problems Solved')
    plt.legend()
    plt.show()


def main():
    show_score_over_time(['20268', '36720', '38388', '171690', '171692'])  # Luis, Renan, Marcelo, Gabriel, Paola
    show_problem_solved_by_category(['171692', '36720'], ['Iniciante', 'Grafos', 'Paradigmas'])  # Luis, Renan


if __name__ == '__main__':
    main()
