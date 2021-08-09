#Aluno: Fabrizio Honda
#Curso: Licenciatura em Computação
#Matéria: Fundamentos Teoricos da Computação
#Professora: Elloá B. Guedes
#Projeto Prático III: Simulando uma Máquina de Turing com Python


def q0():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    while  fita1[cabecote1] != '+':
        if fita1[cabecote1] == '1':
            fita2[cabecote2] = '1'
        elif fita1[cabecote1] == '0':
            fita2[cabecote2] = '0'
        elif fita1[cabecote1] == '*':
            break
        cabecote1+= 1
        cabecote2+= 1
        cabecote3+= 1
        cabecote4+= 1
    if fita1[cabecote1] == '+':
        cabecote1+= 1
        q1()
    else:
        cabecote1-=1
        while fita1[cabecote1] != '*': cabecote1-=1
        cabecote1+=1
        while fita1[cabecote1]!='*':
            print(fita1[cabecote1],end='')
            cabecote1+=1
        print(resultado, end='')

def q1():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4    
    while fita1[cabecote1] != '*':
        cabecote1+=1
    cabecote1-=1
    q2()

def q2():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4   
    while fita1[cabecote1] != '+':
        if fita1[cabecote1] == '1':
            cabecote1-=1
            cabecote3-=1
            fita3[cabecote3] = '1'
        if fita1[cabecote1] == '0':
            cabecote1-=1
            cabecote3-=1
            fita3[cabecote3] = '0'
    q3()

def q3():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    while fita3[cabecote3] != '*':
        cabecote3+=1
    q4()

def q4():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    while fita1[cabecote1] != '*':
        cabecote1+=1
    fita1[cabecote1] = '='
    q5()

def q5():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    cabecote2-=1
    cabecote3-=1
    cabecote4-=1
    vaium = 0
    while fita2[cabecote2] != '*' or fita3[cabecote3] != '*' or vaium == 1:
        if fita2[cabecote2] == '0' and fita3[cabecote3] == '1' and vaium == 0:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '*' and fita3[cabecote3] == '0' and vaium == 0:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '0' and fita3[cabecote3] == '*' and vaium == 0:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '0' and vaium == 0:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '0' and fita3[cabecote3] == '0' and vaium == 0:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '*' and fita3[cabecote3] == '1' and vaium == 0:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '*' and vaium == 0:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '1' and vaium == 0:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
            vaium = 1  
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '1' and vaium == 1:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '0' and fita3[cabecote3] == '1' and vaium == 1:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '*' and fita3[cabecote3] == '0' and vaium == 1:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
            vaium = 0
        elif fita2[cabecote2] == '0' and fita3[cabecote3] == '*' and vaium == 1:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
            vaium = 0
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '0' and vaium == 1:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '0' and fita3[cabecote3] == '0' and vaium == 1:
            fita4[cabecote4] = '1'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
            vaium = 0
        elif fita2[cabecote2] == '*' and fita3[cabecote3] == '1' and vaium == 1:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '1' and fita3[cabecote3] == '*' and vaium == 1:
            fita4[cabecote4] = '0'
            cabecote2-=1
            cabecote3-=1
            cabecote4-=1
        elif fita2[cabecote2] == '*' and fita3[cabecote3] == '*' and vaium == 1:
            fita4[cabecote4] = '1'
            vaium = 0
            
    if fita4[cabecote4] == '*':
        cabecote4+=1
    q6()

def q6():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    while fita4[cabecote4] != '*':
        cabecote1+=1
        if fita4[cabecote4] == '0':
            fita1[cabecote1] = '0'
            cabecote4+=1
        elif fita4[cabecote4] == '1':
            fita1[cabecote1] = '1'
            cabecote4+=1
    qaceita()

def qaceita():
    global fita1, fita2, fita3, fita4
    global cabecote1, cabecote2, cabecote3, cabecote4
    while fita1[cabecote1] != '*':
        cabecote1-=1
    cabecote1+=1
    while fita1[cabecote1] != '*':
        print(fita1[cabecote1],end='')
        cabecote1+=1
    resultado = ' ACEITA'
    print(resultado,end='')
            
    

#Criando as fitas
fita1 = []
fita2 = []
fita3 = []
fita4 = []

#Inicializando os cabeçotes
cabecote1 = 0
cabecote2 = 0
cabecote3 = 0
cabecote4 = 0

#Posicionando cabeçotes no meio
entrada = input()
while cabecote1 < (len(entrada)/2):
    cabecote1+=1
    cabecote2+=1
    cabecote3+=1
    cabecote4+=1
    
#Inicializando as fitas com * 
for i in range(1000):
    fita1.append('*')
    fita2.append('*')
    fita3.append('*')
    fita4.append('*')

    
#Preenchendo a entrada no meio pra simular uma fita infinita
for i in range(len(entrada)):
    fita1[cabecote1] = entrada[i]
    cabecote1+=1

#Cabeçote 1 posiciona-se no começo da entrada
cabecote1 = cabecote2

resultado = ' REJEITA'
q0()
