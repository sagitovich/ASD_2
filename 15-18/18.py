def subset_sum(S, target):
    S.sort(reverse=True)
    subset = []
    total = 0

    for elem in S:
        if total + elem <= target:
            subset.append(elem)
            total += elem

    return subset


# Пример использования
S = [4, -3, 2, 1, 6, -1]
target = 5
print(subset_sum(S, target))
#  6 4 2 1 -1 -3