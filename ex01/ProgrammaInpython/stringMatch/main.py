from naive_KMP import kmp
from naive_KMP import ingenuo
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys
import string

sys.setrecursionlimit(10 ** 9)


def generazioneRandomString(lunghezza):
    carattere = string.ascii_letters + string.digits
    return ''.join(random.choice(carattere) for _ in range(lunghezza))


def misuraTempiIngenuo(testo, pattern):
    start = timer()
    ingenuo(testo, pattern)
    stop = timer()
    return stop - start


def misuraTempiKmp(testo, pattern):
    start = timer()
    kmp(testo, pattern)
    stop = timer()
    return stop - start


def applicazioneAlgoritmi(testo, pattern):

    patter = generazioneRandomString(pattern)
    t_ingenuo = misuraTempiIngenuo(testo, patter)
    t_kmp = misuraTempiKmp(testo, patter)

    return t_ingenuo, t_kmp

def risultatiTempi(tempi1, tempi2):
    t1, t2, t3 = 0, 0, 0
    for i in range(len(tempi1)):
        t1 += tempi1[i]
        t2 += tempi2[i]

    print('\nMediamente...')
    t_max = max(t1, t2)
    if t_max == t1:
        print('Ingenuo ci mette più tempo!')
    elif t_max == t2:
        print('Kmp ci mette più tempo!')

    t_min = min(t1, t2)
    if t_min == t1:
        print('Ingenuo ci mette meno tempo!')
    elif t_min == t2:
        print('Kmp ci mette meno tempo!')

def stampaFigure(titolo, x_lab, y_lab, x, ingenuo, kmp1):
    figura = plt.figure()
    plt.title(titolo)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.plot(x, ingenuo, color='red', label='INGENUO')
    plt.plot(x, kmp1, label='KMP')
    plt.legend()
    return figura


def test(num_test, iterazioni, lunghezza_testo, lunghezza_pattern):
    t_ingenuo, t_kmp = list(), list()
    x = list()

    for i in range(num_test):
        testo_inseriti = 0

        valori_max = generazioneRandomString(lunghezza_testo * iterazioni)

        for j in range(iterazioni):
            testo_inseriti += lunghezza_testo
            if i == 0:
                x.append(testo_inseriti)
                t_ingenuo.append(0)
                t_kmp.append(0)
            valori = valori_max[:testo_inseriti]
            risultati = applicazioneAlgoritmi(valori, lunghezza_pattern)
            t_ingenuo[j] += (risultati[0] / num_test)
            t_kmp[j] += (risultati[1] / num_test)

            # A ogni 5000 inseriti controllo la situazione
            if testo_inseriti % 5000 == 0:
                print("\nTest numero:", i + 1, '\nLunghezza inserita:', testo_inseriti)
            if j % iterazioni == 0:
                print("----------------------------------------------")

            risultatiTempi(t_ingenuo, t_ingenuo)

    first_fig = stampaFigure('Tempi Algorithm', 'String Lunghezza', 'Tempo', x,
                             t_ingenuo, t_kmp)
    first_fig.savefig("Tempi_Algorithm.png", dpi=300)

    plt.legend(['Ingenuo', 'KMP'])


if __name__ == '__main__':
    num_test_ = 5
    iterazioni_ = 10
    lunghezza_testo_ = 5000
    lunghezza_pattern_ = 4

    test(num_test_, iterazioni_, lunghezza_testo_, lunghezza_pattern_)
    plt.show()
