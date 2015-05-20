import numpy as np
import matplotlib.pyplot as plt


y = np.array(input("Digite os valores da variavel dependente do primeiro sinal: "),dtype=float)
pos_inicial_y = input("Digite o valor de início: ")
tam_y = np.size(y)


y1 = np.array(input("Digite os valores da variavel dependente do segundo sinal: "),dtype=float)
pos_inicial_y1 = input("Digite o valor de início: ")
tam_y1 = np.size(y1)

x = np.arange(pos_inicial_y, tam_y+pos_inicial_y)
x1 = np.arange(pos_inicial_y1, tam_y1+pos_inicial_y1)






#faz o gráfico
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.scatter(x, y)
ax1.axhline(0, color='black', lw=1)
ax1.grid(True)

ax2 = fig.add_subplot(212)
ax2.scatter(x1, y1)
ax2.axhline(0, color='black', lw=1)
ax2.grid(True)

plt.bar(x, y, facecolor='#9999ff', edgecolor='white')

plt.show();
