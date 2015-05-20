import numpy as np
import matplotlib.pyplot as plt

#cria o array do primeiro sinal
y = np.array(input("Digite os valores da variavel dependente do primeiro sinal: "),dtype=float)
pos_inicial_y = input("Digite o valor de início: ")
#pega o tamanho do array do primeiro sinal
tam_y = np.size(y)

#cria o array do primeiro sinal
y1 = np.array(input("Digite os valores da variavel dependente do segundo sinal: "),dtype=float)
pos_inicial_y1 = input("Digite o valor de início: ")
#pega o tamanho do segundo array
tam_y1 = np.size(y1)


#faz o eixo do X para o grafico do primeiro sinal começando do 0
#x = np.arange(0, tam_y)
#faz o eixo do X para o grafico do segundo sinal começando do 0
#x1 = np.arange(0, tam_y1)


#faz o eixo do X para o grafico do primeiro sinal
x = np.arange(pos_inicial_y, tam_y+pos_inicial_y)

#faz o eixo do X para o grafico do segundo sinal
x1 = np.arange(pos_inicial_y1, tam_y1+pos_inicial_y1)



#faz o eixo do X para o segundo sinal rebatido
pos_ini_rebatido = tam_y1-(pos_inicial_y1+1)
x1_rebatido = np.arange(-pos_ini_rebatido, pos_inicial_y1+1)

print(x1_rebatido)

print(pos_inicial_y1)


fig = plt.figure()
#faz o gráfico do primeiro sinal
ax1 = fig.add_subplot(2, 2, 1)
ax1.scatter(x, y)
ax1.axhline(0, color='black', lw=1)
ax1.grid(True)
ax1.set_xlabel('Primeiro sinal')


#faz o gráfico do segundo sinal 
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(x1, y1)
ax2.axhline(0, color='black', lw=1)
ax2.grid(True)
ax2.set_xlabel('Segundo sinal')



g_rebate = fig.add_subplot(2, 2, 4)
g_rebate.scatter(x1_rebatido, y1)
g_rebate.axhline(0, color='black', lw=1)
g_rebate.grid(True)
g_rebate.set_xlabel('Segundo sinal rebatido')


#plt.bar(x, y, facecolor='#9999ff', edgecolor='white')

plt.show();
