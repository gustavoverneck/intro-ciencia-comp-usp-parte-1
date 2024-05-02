def remove_repetidos(x):
    items = []
    for i in x:
        if i not in items:
            items.append(i)
        count = 0
        for j in x:
            if i == j:
                if count == 0:
                    count += 1
    return items