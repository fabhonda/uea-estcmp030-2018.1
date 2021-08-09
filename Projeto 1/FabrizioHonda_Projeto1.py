#Aluno: Fabrizio Honda
#Curso: Licenciatura em Computação
#Matéria: Fundamentos Teoricos da Computação
#Professora: Elloá B. Guedes

import re
try:
    dados = input()
    notafiscal = re.match(r'((([\d]{3}\.[\d]{3}\.[\d]{3}-[\d]{2})\s([\d]{2}\.[\d]{3}\.[\d]{3}/[\d]{4}-[\d]{2}|[\d]{3}\.[\d]{3}\.[\d]{3}-[\d]{2})\s([\d]{4}\.[0][^02]\.[0][1-9]|[\d]{4}\.[0][^02]\.[1][0-9]|[\d]{4}\.[0][^02]\.[2][0-9]|[\d]{4}\.[0][^02]\.[3][0-1]|[\d]{4}\.[1][0-2]\.[0][1-9]|[\d]{4}\.[1][0-2]\.[1][0-9]|[\d]{4}\.[1][0-2]\.[2][0-9]|[\d]{4}\.[1][0-2]\.[3][0-1]|[\d]{4}\.02\.[0][1-9]|[\d]{4}\.02\.[1][0-9]|[\d]{4}\.02\.[2][0-9])\s([0-1][\d]:[0-5][\d]:[0-5][\d]|[2][0-3]:[0-5][\d]:[0-5][\d])\s(\[[\d]{1,}\.[\d]{2}\]|\[[\d]{1,}\.[\d]{2}(,[\d]{1,}\.[\d]{2})+\])\s([\d]{9}-[a-z0-9]{5}-[0,2,4,6,8]{3}-[0-1]{3}|[\d]{9}-[a-z0-9]{5}-[0,2,4,6,8]{3}$))$|\n)',dados)

    
    def validacao(n):
        if (len(notafiscal.group(n)) == 14):
            cpf = []
            for i in range(11):
                    cpf.append(notafiscal.group(n)[i])
            #print(cpf)        
            for i in cpf:
                if i == '.':
                    cpf.remove(i)
            #print(cpf) 
            cpf = list(map(int, cpf))
            #print(cpf)

            soma=0
            j=10
            for i in range(9):
                soma+=((cpf[i])*j)
                j=j-1
            #print(soma) 
            
            primeiro=0
            soma=soma%11
            if soma<2:
                primeiro=(str(0))
            else:
                primeiro=(str(11-soma))
            #print(primeiro) 
            #print(notafiscal.group(n)[12])
            if(notafiscal.group(n)[12]!= primeiro):
                return 0
            
            else:
                soma2=0
                j=11
                for i in range(9):
                    soma2+=((cpf[i])*j)
                    j=j-1
                #print(j) 
                soma2+=((int(primeiro))*2)
                #print(soma2) 
                
                segundo=0
                soma2=soma2%11
                if soma2<2:
                    segundo=(str(0))
                else:
                    segundo=(str(11-soma2))
                #print(segundo) 
                #print(notafiscal.group(n)[13]) 
                if notafiscal.group(n)[13]!= segundo:
                    return 0
                else:
                    if (notafiscal.group(n)[0] == notafiscal.group(n)[1]) and (notafiscal.group(n)[0] == notafiscal.group(n)[2]) and (notafiscal.group(n)[0] == notafiscal.group(n)[4]) and (notafiscal.group(n)[0] == notafiscal.group(n)[5]) and (notafiscal.group(n)[0] == notafiscal.group(n)[6]) and (notafiscal.group(n)[0] == notafiscal.group(n)[8]) and (notafiscal.group(n)[0] == notafiscal.group(n)[9]) and (notafiscal.group(n)[0] == notafiscal.group(n)[10]) and (notafiscal.group(n)[0] == notafiscal.group(n)[12]) and (notafiscal.group(n)[0] == notafiscal.group(n)[13]):
                        return 0
                    else:
                        if n==4:
                            iguais=0
                            for i in range(14):
                                if notafiscal.group(3)[i] == notafiscal.group(4)[i]:
                                    iguais=iguais+1
                            if iguais == 14:
                                return 0
                            else:
                                return 1
                        else:
                            return 1
   
        else:
            cnpj = []
            for i in range(15):
                cnpj.append(notafiscal.group(n)[i])
            #print(cnpj) 
            for i in cnpj:
                if i == '.' or i == '/':
                    cnpj.remove(i)
            #print(cnpj) 
            cnpj = list(map(int, cnpj))
            #print(cnpj) 
            
            soma=0
            j=5
            for i in range(12):
                if i<=3:
                    soma+=((cnpj[i])*j)
                    j=j-1
                if i==4:
                    j=9
                    soma+=((cnpj[i])*j)
                if i>4:
                    j=j-1
                    soma+=(cnpj[i]*j)
            #print(soma) 
            
            primeiro=0
            soma=soma%11
            if soma<2:
               primeiro=(str(0))
            else:
                primeiro=(str(11-soma))
            #print(soma) 
            #print(primeiro) 
            #print(notafiscal.group(n)[16]) 
            if(notafiscal.group(n)[16]!= primeiro):
                return 0

            else:
                soma2=0
                j=6
                for i in range(12):
                    if i<5:
                        soma2+=((cnpj[i])*j)
                        j=j-1

                    if i==5:
                        j=9
                        soma2+=((cnpj[i])*j)

                    if i>5:
                        j=j-1

                        soma2+=(cnpj[i]*j)

                soma2+=((int(primeiro))*2)
                #print(soma2) 

                segundo=0
                soma2=soma2%11
                if soma2<2:
                    segundo=(str(0))
                else:
                    segundo=(str(11-soma2))
                #print(segundo) 
                #print(notafiscal.group(n)[17]) 
                if notafiscal.group(n)[17]!= segundo:
                    return 0
                else:
                    if (notafiscal.group(n)[0] == notafiscal.group(n)[1]) and (notafiscal.group(n)[0] == notafiscal.group(n)[3]) and (notafiscal.group(n)[0] == notafiscal.group(n)[4]) and (notafiscal.group(n)[0] == notafiscal.group(n)[5]) and (notafiscal.group(n)[0] == notafiscal.group(n)[7]) and (notafiscal.group(n)[0] == notafiscal.group(n)[8]) and (notafiscal.group(n)[0] == notafiscal.group(n)[9]) and (notafiscal.group(n)[0] == notafiscal.group(n)[11]) and (notafiscal.group(n)[0] == notafiscal.group(n)[12]) and (notafiscal.group(n)[0] == notafiscal.group(n)[13]) and (notafiscal.group(n)[0] == notafiscal.group(n)[14]) and (notafiscal.group(n)[0] == notafiscal.group(n)[16]) and (notafiscal.group(n)[0] == notafiscal.group(n)[17]):
                        return 0
                    else:
                        return 1



    if notafiscal:
        cpf_comprador = validacao(3)
        if cpf_comprador != 0:
            vendedor = validacao(4)
            if vendedor != 0:
                if notafiscal.group(9)[10] == notafiscal.group(9)[11] or notafiscal.group(9)[10] == notafiscal.group(9)[12] or notafiscal.group(9)[10] == notafiscal.group(9)[13] or notafiscal.group(9)[10] == notafiscal.group(9)[14] or notafiscal.group(9)[10] == notafiscal.group(9)[15] or notafiscal.group(9)[11] == notafiscal.group(9)[12] or notafiscal.group(9)[11] == notafiscal.group(9)[13] or notafiscal.group(9)[11] == notafiscal.group(9)[14] or notafiscal.group(9)[12] == notafiscal.group(9)[13] or notafiscal.group(9)[12] == notafiscal.group(9)[14] or notafiscal.group(9)[13] == notafiscal.group(9)[14]:
                    print(False)
                    
                else:
                    print(True)
            else:
                print(False)

        else:
            print(False)

    
    else:
        print(False)

except EOFError:
    print(True)

#group 3 - cpf do comprador
#group 4 - cpf do vendedor ou cnpj da empresa
#group 5 - ano.mês.dia
#group 6 - hora:minuto:segundo 
#group 7 - preços
#group 9 - codigo de transação
