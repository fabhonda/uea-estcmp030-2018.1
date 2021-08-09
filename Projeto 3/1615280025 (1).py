def q0():
    global fita1,fita2,fita3,fita4,fita5,fita6,fita7,cabecote1,cabecote2,cabecote3,cabecote4,cabecote5,cabecote6,cabecote7
    if(fita1[cabecote1]=='a'):
        fita2.append(fita1[cabecote1])
        cabecote1+=1
        cabecote2+=1
        q0()
    elif(fita1[cabecote1]=='b'):
        fita3.append(fita1[cabecote1])
        cabecote1+=1
        cabecote3+=1
        q0()
    elif(fita1[cabecote1]=='c'):
        fita4.append(fita1[cabecote1])
        cabecote1+=1
        cabecote4+=1
        q0()
    elif(fita1[cabecote1]=='d'):
        fita5.append(fita1[cabecote1])
        cabecote1+=1
        cabecote5+=1
        q0()
    elif(fita1[cabecote1]=='e'):
        fita6.append(fita1[cabecote1])
        cabecote1+=1
        cabecote6+=1
        q0()
    elif(fita1[cabecote1]=='f'):
        fita7.append(fita1[cabecote1])
        cabecote1+=1
        cabecote7+=1
        q0()
    elif(fita1[cabecote1]=='#'):
        fita2.append('#')
        fita3.append('#')
        fita4.append('#')
        fita5.append('#')
        fita6.append('#')
        fita7.append('#')
        q1()

def q1():
    global fita1,fita2,fita3,fita4,fita5,fita6,fita7,cabecote1,cabecote2,cabecote3,cabecote4,cabecote5,cabecote6,cabecote7
    if(fita1[cabecote1]=='#' and fita2[cabecote2]=='#' and fita3[cabecote3]=='#' and fita4[cabecote4]=='#' and fita5[cabecote5]=='#' and fita6[cabecote6]=='#' and fita7[cabecote7]=='#'):
        cabecote2-=1
        cabecote3-=1
        cabecote4-=1
        cabecote5-=1
        cabecote6-=1
        cabecote7-=1
        q1()
    elif(fita1[cabecote1]=='#' and fita2[cabecote2]=='a' and fita3[cabecote3]=='b' and fita4[cabecote4]=='c' and fita5[cabecote5]=='d' and fita6[cabecote6]=='e' and fita7[cabecote7]=='f'):
        cabecote2-=1
        cabecote3-=1
        cabecote4-=1
        cabecote5-=1
        cabecote6-=1
        cabecote7-=1
        q1()
    elif(fita1[cabecote1]=='#' and fita2[cabecote2]=='$' and fita3[cabecote3]=='$' and fita4[cabecote4]=='$' and fita5[cabecote5]=='$' and fita6[cabecote6]=='$' and fita7[cabecote7]=='$'):
        q2()
def q2():
    global resultado
    resultado='ACEITA'
try:
    fita1=[]
    cabecote1=1
    fita2=['$']
    cabecote2=1
    fita3=['$']
    cabecote3=1
    fita4=['$']
    cabecote4=1
    fita5=['$']
    cabecote5=1
    fita6=['$']
    cabecote6=1
    fita7=['$']
    cabecote7=1
    resultado='REJEITA'
    fita1=input()
    var=fita1
    fita1='$'+fita1+'#'
    q0()
    print(var,resultado)
except(EOFError):
    print(" ACEITA")




        
