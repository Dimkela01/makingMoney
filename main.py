import numpy as np
import matplotlib.pyplot as plt
from tunnels import find_variance, find_tunel, find_support_line
#import csv

#Update realtime coordinates using csv reader

# with open('coordinates.txt') as coordinates_csv:
#     csv_reader = csv.reader(coordinates_csv, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

t = np.array([i for i in range(1, 101)])
x = 0.5 * t + 3 * (np.sin(t) / t)

varX = find_variance(x)
k1, n1, k2, n2 = find_tunel(t,x,10000,1,0.9)
print(f"k1 = {k1}, n1 = {n1}, k2 = {k2}, n2 = {n2}")
k3, n3 = find_support_line(t, x, 0.1, 0.1, 1)
print(f"k3 = {k3}, n3 = {n3}")

ones = [1 for i in range(len(t))]
tunnel_up = np.array(ones) * k1 * t + n1
tunnel_down = np.array(ones) * k2 * t + n2

#use matplotlib to draw graphs

plt.figure(1)
plt.plot(t, x)
plt.plot(t, tunnel_up)
plt.plot(t, tunnel_down)
plt.xlabel("t")
plt.ylabel("Signal")
plt.grid()
plt.show()





