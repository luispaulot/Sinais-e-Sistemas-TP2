import numpy as np
import matplotlib.pyplot as pl
n = 12
X = np.arange(n)
Y1 = [0,1,2,3,4,5,6,7,8,9,10,11]
Y2 = [0,1,2,3,4,5,-6,-7,8,-9,10,-11]

pl.bar(X, Y1, facecolor='#9999ff', edgecolor='white')
pl.bar(X, Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    pl.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')


pl.subplot(2, 2, 1)
pl.subplot(2, 2, 3)



pl.show()
