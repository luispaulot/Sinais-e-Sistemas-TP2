import numpy as np
import matplotlib.pyplot as plt
import copy

#cria o array do primeiro sinal
y = np.array(input("Digite os valores da variavel dependente do primeiro sinal: "),dtype=float)
pos_inicial_y = input("Digite o valor de início: ")
#pega o tamanho do array do primeiro sinal
tam_y = np.size(y)
#teste
print(y)

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
#Testando...
#print(x1_rebatido)
#testando...
#print(pos_inicial_y1)


#cria um vetor de eixo X que cabe todos os itens do inicio ao fim da convolução
#x_convolucao = np.arange(-pos_ini_rebatido, tam_y+pos_inicial_y+tam_y)
#print(x_convolucao)


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


#cria o grafico do sinal rebatido
g_rebate = fig.add_subplot(2, 2, 4)
g_rebate.scatter(x1_rebatido, y1)
g_rebate.axhline(0, color='black', lw=1)
g_rebate.grid(True)
g_rebate.set_xlabel('Segundo sinal rebatido')

#y para convulução
y_p_conv = copy.copy(y)
x_p_conv = np.arange(0, tam_y+tam_y1*2)
print x_p_conv
#zerar todos
for z in range(0,np.size(x_p_conv)):
    x_p_conv[z] = 0

print x_p_conv

#faz o array receber os valores do primeiro sinal nas posições corretas
n = 0
for z in range(tam_y1,tam_y+tam_y1):
    x_p_conv[z] = y_p_conv[n]
    n = n+1

print x_p_conv



#plt.bar(x, y, facecolor='#9999ff', edgecolor='white')

plt.show();
