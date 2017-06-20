from datetime import date
import csv
import math

import matplotlib.pyplot as plt


def load_data(profile_id):
    with open(profile_id + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def date_distance(d, d0):
    dd0, mm0, yy0 = map(int, d0.split('/'))
    dd, mm, yy = map(int, d.split('/'))
    return (date(yy, mm, dd) - date(yy0, mm0, dd0)).days


def score(data, range=None):
    value = 0
    actual_date = data[0][0]
    for problem in data:
        if range and date_distance(problem[0], data[0][0]) > range:
            break
        if actual_date != problem[0]:
            actual_date = problem[0]
            yield date_distance(actual_date, data[0][0]), value
        value += int(problem[-1]) ** math.e


def score_over_time(profiles_ids):
    for id in profiles_ids:
        data = load_data(id)
        x, y = zip(*score(data))
        plt.plot(x, y, label=id)
    plt.title('score')
    plt.xlabel('day')
    plt.ylabel('score')
    plt.legend()
    plt.show()


def main():
    score_over_time(['20268', '36720', '38388', '171690', '171692'])  # Luis, Renan, Marcelo, Gabriel, Paola


if __name__ == '__main__':
    main()