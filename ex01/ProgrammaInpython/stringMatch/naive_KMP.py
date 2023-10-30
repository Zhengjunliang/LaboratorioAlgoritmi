def ingenuo(testo, pattern):

    n = len(testo)
    m = len(pattern)

    if m > n:
        yield -1

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if testo[i + j] != pattern[j]:
                match = False
                break

        if match:
            yield i


def calcolare_prefisso(pattern):

    m = len(pattern)
    prefisso = [0] * m
    lunghezza = 0

    for i in range(1, m):
        while lunghezza > 0 and pattern[lunghezza] != pattern[i]:
            lunghezza = prefisso[lunghezza - 1]

        if pattern[lunghezza] == pattern[i]:
            lunghezza += 1

        prefisso[i] = lunghezza

    return prefisso


def kmp(testo, pattern):

    n = len(testo)
    m = len(pattern)

    if m > n:
        yield -1

    prefisso = calcolare_prefisso(pattern)
    j = 0

    for i in range(n):
        while j > 0 and pattern[j] != testo[i]:
            j = prefisso[j - 1]

        if pattern[j] == testo[i]:
            j += 1

        if j == m:
            yield i - m + 1
            j = prefisso[j - 1]

