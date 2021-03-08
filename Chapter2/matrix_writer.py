with open('out7500.txt', 'a+') as f:
    for i in range(7500):
        for j in range(7500):
            f.write(f'{j} ')
        f.write('\n')