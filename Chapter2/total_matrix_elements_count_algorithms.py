import time
import csv

files = ['out100.txt', 'out1000.txt', 'out5000.txt', 'out7500.txt']


def var1_total_matrix_elements(file: str) -> tuple:
    """A functions that given a file that has a matrix in it will print to screen how much it took and the total
    of the elements in it"""

    start = time.perf_counter()
    a = []
    with open(file, 'r') as f:
        for line in f:
            a.append([int(x) for x in line.split()])

    n = len(a)
    line_sum = []
    total = 0

    for i in range(n):
        line_sum.append(0)
        for j in range(n):
            line_sum[i] += a[i][j]
            total += a[i][j]
    print(f'Total sum is {total}')
    stop = time.perf_counter()
    time_passed = stop - start
    print(time_passed)
    return total, time_passed


def var2_total_matrix_elements(file: str) -> tuple:
    """A functions that given a file that has a matrix in it will print to screen how much it took and the total
    of the elements in it"""

    start = time.perf_counter()

    a = []
    with open(file, 'r') as f:
        for line in f:
            a.append([int(x) for x in line.split()])

    n = len(a)
    line_sum = []
    total = 0

    for i in range(n):
        line_sum.append(0)
        for j in range(n):
            line_sum[i] += a[i][j]
        total += line_sum[i]
    print(f'Total sum is {total}')
    stop = time.perf_counter()
    time_passed = stop - start
    print(time_passed)
    return total, time_passed


# write to CSV the results from the algorithms.
with open('results_algorithm_comparison.csv', mode='a+') as csv_file:
    fieldnames = ['Dimension', 'Version1 time execution', 'Version2 time execution', 'Difference']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for file in files:
        total1, time_passed1 = var1_total_matrix_elements(file)
        total2, time_passed2 = var2_total_matrix_elements(file)
        writer.writerow({
            'Dimension': file,
            'Version1 time execution': time_passed1,
            'Version2 time execution': time_passed2,
            'Difference': time_passed1-time_passed2
        })
