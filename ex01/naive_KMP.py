def naive(text, pattern):
    """Naive string search algorithm.

    :param text: The input text.
    :param pattern: The pattern to search for.
    :return: A generator yielding the starting positions of pattern in text.
    """
    n = len(text)
    m = len(pattern)

    if m > n:
        yield -1

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            yield i


def calculate_prefix(pattern):
    """Calculate the prefix function for the KMP algorithm.

    :param pattern: The pattern.
    :return: A list containing the length of the longest prefix of pattern[i].
    """
    m = len(pattern)
    prefix = [0] * m
    length = 0

    for i in range(1, m):
        while length > 0 and pattern[length] != pattern[i]:
            length = prefix[length - 1]

        if pattern[length] == pattern[i]:
            length += 1

        prefix[i] = length

    return prefix


def kmp(text, pattern):
    """Knuth-Morris-Pratt (KMP) string search algorithm.

    :param text: The input text.
    :param pattern: The pattern to search for.
    :return: A generator yielding the starting positions of pattern in text.
    """
    n = len(text)
    m = len(pattern)

    if m > n:
        yield -1

    prefix_values = calculate_prefix(pattern)
    j = 0

    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = prefix_values[j - 1]

        if pattern[j] == text[i]:
            j += 1

        if j == m:
            yield i - m + 1
            j = prefix_values[j - 1]