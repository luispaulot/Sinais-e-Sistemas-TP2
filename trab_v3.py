import numpy as np
import matplotlib.pyplot as plt
import copy

#cria o array do primeiro sinal
y = np.array(input("Digite os valores da variavel dependente do primeiro sinal: "),dtype=float)
pos_inicial_y = 0 #Neste trabalho escolhi começar sempre do zero no eixo do tempo
#pega o tamanho do array do primeiro sinal
tam_y = np.size(y)


#cria o array do primeiro sinal
y1 = np.array(input("Digite os valores da variavel dependente do segundo sinal: "),dtype=float)
pos_inicial_y1 = 0 #Neste trabalho escolhi começar sempre do zero no eixo do tempo
tam_y1 = np.size(y1)



#faz o eixo do X para o grafico do primeiro sinal
x = np.arange(pos_inicial_y, tam_y+pos_inicial_y)

#faz o eixo do X para o grafico do segundo sinal
x1 = np.arange(pos_inicial_y1, tam_y1+pos_inicial_y1)


#rebate o segundo sinal
x1_rebatido = np.arange(0, tam_y1)
if (tam_y1 == 1):
    x1_rebatido = y1
else:
    
    c = copy.copy(tam_y1-1)
    for z in range(0,tam_y1):
        x1_rebatido[z] = y1[c]
        c = c-1
#fim de rebatimento
    


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


#cria array para X
txx = np.arange(0,tam_y+tam_y1*2)
#zera o vetor
for z in range(0,tam_y+tam_y1*2):
    txx[z] = 0

print txx

#coloca os valores de X em XX
n = 0
for z in range(tam_y1, tam_y1+tam_y):
    txx[z] = y[n]
    n = n+1

print txx

#cria eixo de x para convolução
eixo_conv = np.arange(0,tam_y+tam_y1*2)
#pega o tamanho do eixo de convolução
conv_print = copy.copy(eixo_conv)

#zera o vetor
for z in range(0,tam_y+tam_y1*2):
    eixo_conv[z] = 0

print eixo_conv



#cria o grafico do sinal rebatido
g_rebate = fig.add_subplot(2, 2, 3)
g_rebate.scatter(conv_print, eixo_conv)
g_rebate.axhline(0, color='black', lw=1)
g_rebate.grid(True)
g_rebate.set_xlabel('Soma de convolucao dos sinais')

plt.show();





