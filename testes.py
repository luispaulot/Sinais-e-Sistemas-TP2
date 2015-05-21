#testes
import numpy as np
import copy

x = np.array([9,9,9])

y = np.arange(0,7)


n = 0
for v in range(2,5):
    y[v] = x[n]
    n = n+1


print y

