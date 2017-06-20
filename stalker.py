import os
import re
import sys

import problemparser
import statistics

def flag_to_category(flags):
    category = {
        'I': 'Iniciante', 'A': 'Ad-Hoc',
        'S': 'Strings', 'E': 'Estruturas e Bibliotecas',
        'M': 'Matemática', 'P': 'Paradigmas',
        'G': 'Grafos', 'C': 'Geometria Computacional'
    }
    categories = []
    for flag in flags:
        if flag in category:
            categories.append(category[flag])
    return categories

cmd = ' '.join(sys.argv[1:])

profiles_ids = [i for i in cmd.split() if i.isdigit()]

for profile_id in profiles_ids:
    if not os.path.exists(profile_id + '.csv'):
        print('info: %s não está na base de dados, baixando dados...' % profile_id)
        problemparser.problemparser(profile_id)
        print('info: dados já fazem parte da base de dados.')

if 'show-score' in cmd:
    statistics.show_score_over_time(profiles_ids)
elif 'show-problems-solved' in cmd:
    flags = re.search('-[A-Z]+', cmd).group()
    categories = flag_to_category(flags)
    statistics.show_problem_solved_by_category(profiles_ids, categories)