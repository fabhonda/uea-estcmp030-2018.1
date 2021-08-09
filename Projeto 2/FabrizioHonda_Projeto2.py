#Aluno: Fabrizio Honda
#Curso: Licenciatura em Computação
#Matéria: Fundamentos Teoricos da Computação
#Professora: Elloá B. Guedes
#Projeto Prático II: Representação Matricial de AFDs

import ast

def validacao(dicionario,palavra):

#Ordenando a Matriz Delta
    for i in range(len(dicionario['delta'])):
        dicionario['delta'][i].sort()
    #print("Matriz Delta ordenada:",dicionario['delta'])

    
#Gerando a Matriz Pi
    matrizPi=[]
    for i in range(dicionario['estados']):
        if i==dicionario['inicial']:
            matrizPi.insert(i,[1])
        else:
            matrizPi.insert(i,[0])
    #print("Matriz Pi:",matrizPi)

#Gerando a Matriz Pi Transposta
    matrizT=[]
    for i in range(dicionario['estados']):
        matrizPi[i] = matrizPi[i][0]
    matrizT.append(matrizPi)
    #print("Matriz Pi Transposta:",matrizT)

#Gerando a Matriz Eta
    matrizEta=[]
    for i in range(dicionario['estados']):
        aceita=0
        for j in range(len(dicionario['final'])):
            if dicionario['final'][j] == i:
                aceita=1
        if aceita == 1:
            matrizEta.insert(i,[1])
        else:
            matrizEta.insert(i,[0])
    #print("Matriz Eta:",matrizEta)

#Gerando a Matriz Xa
    listaA=[]
    for i in range(dicionario['estados']):
        listaA.insert(i,dicionario['delta'][i][0])
    matrizXa=[]
    for i in range(dicionario['estados']):
        matrizXa.append([0] * dicionario['estados'])
        matrizXa[i][listaA[i]] = 1
    #print("Matriz Xa:",matrizXa)

#Gerando a Matriz Xb
    listaB=[]
    for i in range(dicionario['estados']):
        listaB.insert(i,dicionario['delta'][i][1])
    matrizXb=[]
    for i in range(dicionario['estados']):
        matrizXb.append([0] * dicionario['estados'])
        matrizXb[i][listaB[i]] = 1
    #print("Matriz Xb:",matrizXb)

#Inicializando Xw de tamanho 1xdicionario['estados']
    matrizXw=[]
    for i in range(1):
        matrizXw.append([0] * dicionario['estados'])
    #print("Matriz Xw zerada:",matrizXw)

     
#Matriz Pi Transposta x (Matriz Xa ou Matriz Xb)
    if palavra[0] == 'a':
        for i in range(dicionario['estados']):
            for j in range(dicionario['estados']):
                linha = 0
                for k in range(dicionario['estados']):
                    linha = linha + matrizT[0][k] * matrizXa[k][j]
                matrizXw[0][j] = linha
        #print("Matriz Xw com Xa inicial:",matrizXw)

    elif palavra[0] == 'b':
        for i in range(dicionario['estados']):
            for j in range(dicionario['estados']):
                linha = 0
                for k in range(dicionario['estados']):
                    linha = linha + matrizT[0][k] * matrizXb[k][j]
                matrizXw[0][j] = linha
        #print("Matriz Xw com Xb inicial:",matrizXw)
      
#Multiplicação de Xw com Eta 
    if len(palavra) == 1:
        for i in range(dicionario['estados']):
            linha = 0
            for k in range(dicionario['estados']):
                linha = linha + matrizXw[0][k] * matrizEta[k][0]
            elemento = linha
        #print(elemento)
        return elemento

#Incrementando Xw se a palavra tiver tamanho maior que 1
    elif len(palavra) > 1:
        for i in range(1,(len(palavra))):
            if palavra[i] == 'a':
                aux=[]
                for j in range(dicionario['estados']):
                    linha = 0
                    for k in range(dicionario['estados']):
                        linha = linha + matrizXw[0][k] * matrizXa[k][j]
                    aux.insert(j,linha)
                    #print("auxiliar de a:",aux)
                for i in range(dicionario['estados']):
                    matrizXw[0][i] = aux[i]

            elif palavra[i] == 'b':
                aux=[]
                for j in range(dicionario['estados']):
                    linha = 0
                    for k in range(dicionario['estados']):
                        linha = linha + matrizXw[0][k] * matrizXb[k][j]
                    aux.insert(j,linha)
                    #print("auxiliar de b:",aux)
                for i in range(dicionario['estados']):
                    matrizXw[0][i] = aux[i]
                    
        for i in range(dicionario['estados']):
            linha = 0
            for k in range(dicionario['estados']):
                linha = linha + matrizXw[0][k] * matrizEta[k][0]
            elemento = linha
        #print(elemento)
        return elemento
        
      



#Começo do código
dicionario = ast.literal_eval(input())
inteiro = int(input())
for i in range(inteiro):
    palavra = input()
    saida = validacao(dicionario,palavra)
    if saida==1:
        print("ACEITA")
    elif saida==0:
        print("REJEITA")




#{'estados':2, 'inicial' : 0, 'final':[1], 'delta' : [[0,1],[0,1]] }
#{'estados': 7 , 'inicial' :  0 , 'final': [1, 3, 4, 6] , 'delta' : [[0, 5], [1, 1], [1, 2], [0, 1], [3, 2], [3, 1], [2, 2]] }
#{'estados': 3 , 'inicial' :  0 , 'final': [1, 2] , 'delta' : [[0, 1], [1, 1], [0, 0]] }

