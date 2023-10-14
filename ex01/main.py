from naive_KMP import kmp
from naive_KMP import naive
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys
import string

sys.setrecursionlimit(10 ** 9)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Puoi aggiungere altri caratteri a seconda delle tue esigenze
    return ''.join(random.choice(characters) for _ in range(length))

def misuraTempi(frase, patter):
    start = timer()
    naive(frase, patter)
    stop = timer()
    return stop - start

def misuraTempiKmp(frase, patter):
    start = timer()
    print(list(kmp(frase, patter)))
    stop = timer()
    return stop - start

def creazioneAlberi(frase):

    patter = "a"
    # Test creazione per albero abr
    t_naive = misuraTempi(frase, patter)

    # Test creazione per albero arn
    t_kmp = misuraTempiKmp(frase, patter)

    return t_naive, t_kmp


def risultatiTempi(tempi1, tempi2):
    t1, t2 = 0, 0
    for i in range(len(tempi1)):
        t1 += tempi1[i]
        t2 += tempi2[i]
    print('\nMediamente...')
    t_max = max(t1, t2)
    if t_max == t1:
        print('ABR ci mette più tempo!')
    elif t_max == t2:
        print('ARN ci mette più tempo!')

    t_min = min(t1, t2)
    if t_min == t1:
        print('ABR ci mette meno tempo!')
    elif t_min == t2:
        print('ARN ci mette meno tempo!')
    print(t1,t2)

def stampaFigure(title, x_lab, y_lab, x, abr, arn):
    figura = plt.figure()
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.plot(x, abr, color='red', label='ABR')
    plt.plot(x, arn, label='ARN')
    plt.legend()
    return figura


def test(num_test, iterazioni, num_nodi):
    t_creazione_naive, t_creazione_kmp = list(), list()
    x = list()

    for i in range(num_test):
        nodi_inseriti = 0

        valori_max = generate_random_string(num_nodi * iterazioni)

        for j in range(iterazioni):
            nodi_inseriti += num_nodi
            if i == 0:
                x.append(nodi_inseriti)
                t_creazione_naive.append(0)
                t_creazione_kmp.append(0)
            valori = valori_max[:nodi_inseriti]
            print(valori)
            risultati = creazioneAlberi(valori)
            t_creazione_naive[j] += (risultati[0] / num_test)
            t_creazione_kmp[j] += (risultati[1] / num_test)


            # A ogni 5000 nodi inseriti controllo la situazione
            if nodi_inseriti % 5000 == 0:
                print("\nTest numero:", i + 1, '\nNumero nodi inseriti:', nodi_inseriti)
            if j % iterazioni == 0:
                print("----------------------------------------------")

        risultatiTempi(t_creazione_naive, t_creazione_kmp)

    first_fig = stampaFigure('Tempi Algorithm', 'String lenth', 'Time', x,
                             t_creazione_naive, t_creazione_kmp)
    first_fig.savefig("Tempi_Algorithm.png", dpi=300)

    plt.legend(['Naive', 'KMP'])


if __name__ == '__main__':
    num_test = 2
    iterazioni = 1
    num_nodi = 50
    nodi_inseriti = 0
    test(num_test, iterazioni, num_nodi)
    plt.show()








