#programa 3
def nuevo(dni,trj):
    archivo=open("cliente_sube.txt","a")
    archivo.close()
    archivo=open("cliente_sube.txt","r")
    datos=archivo.readline()

    while (datos!=""):
        aux=datos.split(",",8)
        if(int(aux[7]) != int(trj)):
            if (int(aux[2])==int(dni)):
                return(True)
        datos=archivo.readline()
def alta():
    cont = 0
    archivo = open ("cliente_sube.txt","a")
    archivo.close()
    apellido = input("Ingrese el Apellido: ")
    nombre = input("Ingrese el Nombre: ")
    archivo = open ("cliente_sube.txt","r")
    datos = archivo.readline()
    dni = int(input("Ingrese el DNI: "))
    while(len(str(dni)) != 8):
        print("\nERROR\n")
        dni = int(input("Ingrese el DNI: "))
    while(datos != ""):
        aux = datos.split(",",12)
        aux2 = int(aux[5])
        cont+=1
        
        while(aux2 == dni):
            print("\nERROR\nDNI existente\n")
            dni = int(input("Ingrese el DNI: "))
        datos = archivo.readline()
    if(cont == 0):
        dni = dni
    archivo.close()
    print("\nIngrese sexo\n")
    op=int(input("1)Masculino.\n2)Femenino.\n3)No Binario\n\n"))
    while(op != 1 and op != 2 and op !=3):
        print("\nERROR\n")
        op=int(input("1)Masculino.\n2)Femenino.\n3)No Binario\n\n"))        
    if(op == 1):
        genero = str("M")
    if(op == 2):
        genero = str("F")
    if(op == 3):
       genero = str("B")
    print("\nIngrese fecha de Nacimiento\n")
    mes=int(input("Ingrese el mes: "))
    while(mes > 12 or mes <= 0):
        print("\nERROR\n")
        mes=int(input("Ingrese el mes: "))
    dia=int(input("Ingrese el dia: "))
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    while(dia>dias[mes-1] or dia<1):
        print("\nERROR\n")
        dia=int(input("Ingrese el dia: "))
    año=int(input("Ingrese el año: "))
    while(año<=1950 or año>2024):
        print("\nERROR\n")
        año=int(input("Ingrese el año: "))
    nacimiento=str(dia)+'/'+str(mes)+'/'+str(año)
    nom_usu = dni
    contrase_usu = dni
    
    contador=open('contador.txt','a')
    contador.close()
    contador=open('contador.txt','r')
    a=str(contador.readline())
    if(a==''):
        a=0
    else:
        a=int(a)
    b=a+1
    tarj = str("6061268200000000")
    tarj = int("6061268200000000")+b
    contador.close()
    print("Su numero de tarjeta es",tarj)
    contador=open('contador.txt','w')
    contador.write(str(b))
    contador.close()
    saldo = 0
    bj = int(1)
    if(b == 1):
        aux = str(apellido.lower())+","+str(nombre.lower())+","+str(dni)+","+str(genero)+","+str(nacimiento)+","+str(nom_usu)+","+str(contrase_usu)+","+str(tarj)+","+str(saldo)+","+str(bj)+"\n"
    elif(b > 1):
        aux = str(apellido.lower())+","+str(nombre.lower())+","+str(dni)+","+str(genero)+","+str(nacimiento)+","+str(nom_usu)+","+str(contrase_usu)+","+str(tarj)+","+str(saldo)+","+str(bj)+"\n"
    archivo = open ("cliente_sube.txt","a")
    archivo.write(aux)
    archivo.close()
    menu()

def modifica():
    cont=0
    cont2=0
    cont3 = 0
    vec=[]
    archivo = open ("cliente_sube.txt","a")
    archivo.close()
    archivo2 = open("temp.txt","w")
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    nr_tarj=int(input("Ingrese el numero de tarjeta para Modificar: "))
    while(len(str(nr_tarj))!=16):
        print("ERROR")
        nr_tarj=int(input("Ingrese el numero de tarjeta para Modificar: "))

    while(datos!=''):
        aux=datos.split(',',12)
        aux2=int(aux[7])
        cont+=1
        if(aux[9] != 0):
            if(aux2!=nr_tarj):
                cont2+=1
                archivo2.write(datos)
            else:
                apellido = input("Ingrese el Apellido: ")
                nombre = input("Ingrese el Nombre: ")
                dni = int(input("Ingrese el DNI: "))
                while(len(str(dni)) != 8):
                    print("\nERROR\n")
                    dni = int(input("Ingrese el DNI: "))
                existe = nuevo(dni,nr_tarj)
                while(existe):
                    print("\nERROR\nDNI ya existente\n")
                    dni = int(input("Ingrese el DNI: "))
                    existe = nuevo(dni,nr_tarj)   
                print("\nIngrese sexo\n")
                op=int(input("1)Masculino.\n2)Femenino.\n3)No Binario\n\n"))
                while(op != 1 and op != 2 and op !=3):
                    print("\nERROR\n")
                    op=int(input("1)Masculino.\n2)Femenino.\n3)No Binario\n\n"))        
                if(op == 1):
                    genero = str("M")
                if(op == 2):
                    genero = str("F")
                if(op == 3):
                   genero = str("B")
                print("\nIngrese fecha de Nacimiento\n")
                mes=int(input("Ingrese el mes: "))
                while(mes > 12 or mes <= 0):
                    print("\nERROR\n")
                    mes=int(input("Ingrese el mes: "))
                dia=int(input("Ingrese el dia: "))
                while(dia>31 or dia<=0):
                    print("\nERROR\n")
                    dia=int(input("Ingrese el dia: "))
                año=int(input("Ingrese el año: "))
                while(año<=0 or año>2024):
                    print("\nERROR\n")
                    año=int(input("Ingrese el año: "))
                nacimiento=str(dia)+'/'+str(mes)+'/'+str(año)
                nom_usu = aux[5]
                contrase_usu = aux[6]
                tarj = aux[7]
                print("Su numero de tarjeta es",tarj)
                saldo = aux[8]
                aux = str(apellido.lower())+","+str(nombre.lower())+","+str(dni)+","+str(genero)+","+str(nacimiento)+","+str(nom_usu)+","+str(contrase_usu)+","+str(tarj)+","+str(saldo)+","+str(aux[9])
                archivo2.write(aux)
        datos=archivo.readline()
    if(cont == cont2 and cont >1 and cont2>=1):
        print("NUMERO DE TARJETA INCORRECTO")
    if(cont<1):
        print("No hay ningun dato.\n")
    archivo.close()
    archivo2.close()
    archivo2 = open ("temp.txt","r")
    archivo = open ("cliente_sube.txt","w")
    aux = archivo2.readline()
    while(aux != ""):
        archivo.write(aux)
        aux = archivo2.readline()
    archivo.close()
    archivo2.close()
    menu()
def baja():
    cont=0
    cont2=0
    cont3 = 0
    archivo = open ("cliente_sube.txt","a")
    archivo.close()
    archivo2 = open("temp.txt","w")
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    nr_tarj=int(input("Ingrese el numero de tarjeta para Baja: "))
    while(len(str(nr_tarj))!=16):
        print("ERROR")
        nr_tarj=int(input("Ingrese el numero de tarjeta para Baja: "))

    while(datos!=''):
        aux=datos.split(',',12)
        aux2=int(aux[7])
        cont+=1
        if(aux2!=nr_tarj):
            cont2+=1
            archivo2.write(datos)
        else:
            aux[9]=str("0"+"\n")
            aux = str(aux[0])+","+str(aux[1])+","+str(aux[2])+","+str(aux[3])+","+str(aux[4])+","+str(aux[5])+","+str(aux[6])+","+str(aux[7])+","+str(aux[8])+","+str(aux[9])
            archivo2.write(aux)
        datos=archivo.readline()
    if(cont == cont2 and cont >1 and cont2>=1):
        print("TARJETA INCORRECTO")
    if(cont==0):
        print("No hay ningun dato.\n")
    archivo.close()
    archivo2.close()
    archivo2 = open ("temp.txt","r")
    archivo = open ("cliente_sube.txt","w")
    aux = archivo2.readline()
    while(aux != ""):
        archivo.write(aux)
        aux = archivo2.readline()
    archivo.close()
    archivo2.close()
    menu()
def listar():
    cont=0
    cont2=0
    archivo = open ("cliente_sube.txt","a")
    archivo.close()
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    print("Apellido"+"   "+"Nombre"+"   "+"DNI"+"   "+"Genero"+"  "+"Nacimiento"+"  "+"Usuario"+"  "+"Contraseña"+"  "+"Tarjeta"+"  "+"Saldo")
    while(datos!=''):
        cont+=1
        aux=datos.split(',',12)
        
        if(int(aux[9]) != 0):
            cont2+=1
            print(" "+str(aux[0])+" "*3+str(aux[1])+" "*2+str(aux[2])+" "*2+str(aux[3])+" "+str(aux[4])+"-"+str(aux[5])+"-"*2+str(aux[6])+"-"*2+str(aux[7])+"-"*2+str(aux[8]))
        datos=archivo.readline()
    
    if(cont == 0 or cont2 ==0):
        print("No hay ningun dato")
    menu()
def menu():
    opc = int(input("1)Alta.\n2)Modifica.\n3)Baja.\n4)Mostrar Usuarios.\n5)Salir\n\n"))
    if(opc == 5):
        print("chao")
    if(opc == 1):
        alta()
    if(opc == 2):
        modifica()
    if(opc == 3):
        baja()
    if(opc == 4):
        listar()
    
menu()
