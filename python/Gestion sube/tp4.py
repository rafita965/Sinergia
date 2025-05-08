#programa 4
from tp1 import seleccion_linea
def login():
    try:
        archivo = open("cliente_sube.txt","r")
    except:
        print("No hay usuarios registrados")
        exit()
    v1 = False
    v2 = False
    vacio = True
    cont = 0
    cont2 = 0
    archivo = open("cliente_sube.txt","a")
    archivo.close()
    archivo = open("cliente_sube.txt","r")
    aux = archivo.readline()
    usu = input("Ingrese el Usuario: ")
    contra = input("Ingrese la Contraseña: ")
    while(aux != ""):
        cont+=1
        aux2 = aux.split(",",10)
        if(int(aux2[9])!=0):
            cont2+=1
            if(str(aux2[5])== usu):
                print("\nUsuario Correcto\n")
                v1= True
                if(str(aux2[6]) == contra):
                    print("Contraseña correcta\n")
                    v2= True
        else:
            vacio = False
        aux = archivo.readline()
    if(v1 and v2 == True):
        menu(usu,contra)
    if(vacio == False):
        print("\n")
        print("Usuario no encontrado")
def mostrar(usu,contra):
    archivo = open("cliente_sube.txt","r")
    aux = archivo.readline()
    while(aux != ""):
        aux2 = aux.split(",",10)
        if(usu == str(aux2[5]) and contra == str(aux2[6])):
            print("Su saldo es de",float(aux2[8]))
        aux = archivo.readline()
    archivo.close()
    print("\n")
    menu(usu,contra)
def carga_saldo(usu,contra):
    cont = 0
    verdad = True
    archivo = open ("cliente_sube.txt","a")
    archivo.close()
    archivo2 = open("temp.txt","w")
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    while(datos!=''):
        aux=datos.split(',',12)
        aux2=str(aux[5])
        aux3=str(aux[6])
        if(aux2!=usu and aux3 != contra):
            archivo2.write(datos)
        else:
            cont += 1
            opc=float(input("¿Cuanto desea cargar?: \n"))
            nrj_tarjeta=aux[7]
            while(opc >1000):
                print("Error\n")
                opc=float(input("¿Cuanto desea cargar?: \n"))
            if(float(aux[8])+opc <= 3000):
                nuevo_sal = float(aux[8])+opc
                nrj_tarjeta=aux[7]
                aux = str(aux[0])+","+str(aux[1])+","+str(aux[2])+","+str(aux[3])+","+str(aux[4])+","+str(aux[5])+","+str(aux[6])+","+str(aux[7])+","+str(nuevo_sal)+","+str(aux[9])
                archivo2.write(aux)
            else:
                verdad = False
                print("No se puede, se pasa de 3000")
                archivo2.write(datos)
        datos=archivo.readline()
    archivo.close()
    archivo2.close()
    if(verdad == True):
        archivo2 = open ("temp.txt","r")
        archivo = open ("cliente_sube.txt","w")
        aux = archivo2.readline()
        while(aux != ""):
            archivo.write(aux)
            aux = archivo2.readline()
        archivo.close()
        archivo2.close()
        archivo3 = open("movimiento.txt","a")
        movi="Carga"
        aux_movi = str(nrj_tarjeta)+","+str(movi)+","+str(nuevo_sal)+","+str(opc)+"\n"
        archivo3.write(aux_movi)
        archivo3.close()
    print("\n")
    menu(usu,contra)
def cobro(a,usu,contra):
    cont = 0
    valor = True
    maximo = float(90)
    archivo = open("cliente_sube.txt","r")
    aux = archivo.readline()
    while(aux != ""):
        aux2 = aux.split(",",10)
        if(usu == str(aux2[5]) and contra == str(aux2[6])):
            if(float(aux2[8])-float(a[1]) < 0):
                print("Su saldo es de",float(aux2[8]))
                print("Recarge saldo.\nNo puede viajar\n")
                valor =False
                nuevo_sal = aux2[8]
            if(float(aux2[8])>maximo):
                print("Su saldo es de",float(aux2[8])-float(a[1]),"\n")
                nuevo_sal=float(aux2[8])-float(a[1])
            else:
                valor = False
                print("Su saldo es menor",float(aux2[8]),"que",maximo,"el maximo")
                print("Recarge saldo.\nNo puede viajar\n")
        aux = archivo.readline()
    archivo.close()
    if( valor == True):
        archivo2 = open("temp.txt","w")
        archivo = open("cliente_sube.txt","r")
        
        datos=archivo.readline()
        while(datos!=""):
            aux=datos.split(",",12)
            aux2=str(aux[5])
            aux3=str(aux[6])
            if(aux2!=usu and aux3 != contra):
                archivo2.write(datos)
            else:
                nrj_tarjeta = int(aux[7])
                aux[8] = nuevo_sal
                aux4 = str(aux[0])+","+str(aux[1])+","+str(aux[2])+","+str(aux[3])+","+str(aux[4])+","+str(aux[5])+","+str(aux[6])+","+str(aux[7])+","+str(aux[8])+","+str(aux[9])
                archivo2.write(aux4)
            datos=archivo.readline()
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
        archivo = open ("Trenes.txt","r")
        lee= archivo.readlines()
        aux=lee[a[0]].split(" , ",30)
        if(a[1] == maximo):
            movi = str("debito")
        if(a[1] != maximo):
            movi = str("credito")
        archivo3 = open("movimiento.txt","a")
        aux_movi = str(nrj_tarjeta)+","+str(aux[1])+","+str(movi)+","+str(nuevo_sal)+"\n"
        archivo3.write(aux_movi)
        archivo3.close()
    print("\n")
    menu(usu,contra)
def movimientos(usu,contra):
    cont = 0
    cont2 = 0
    cont3 = 0
    archivo3 = open("movimiento.txt","a")
    archivo3.close()
    archivo = open("cliente_sube.txt","a")
    archivo.close()
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    while(datos!=''):
        aux=datos.split(',',12)
        aux2=str(aux[5])
        aux3=str(aux[6])
        cont+=1
        if(aux2 == usu and aux3 == contra):
            n_tarj = int(aux[7])
        datos=archivo.readline()
    archivo.close()
    archivo3 = open("movimiento.txt","r")
    datos=archivo3.readline()
    while(datos!=''):
        aux = datos.split(",",10)
        aux2 = int(aux[0])
        cont2+=1
        if(aux2 == n_tarj):
            cont3+=1
            print(str(aux[0])+" "+str(aux[1])+" "+str(aux[2])+" "+str(aux[3]))
        datos=archivo3.readline()
    if(cont == 0 and cont2 == 0):
        print("No hay ningun dato")
    if(cont3 == 0):
        print("No existe ningun movimiento")
    print("\n")
    menu(usu,contra)
def modifica(usu,contra):
    cont=0
    archivo2 = open("temp.txt","w")
    archivo = open("cliente_sube.txt","r")
    datos=archivo.readline()
    while(datos!=''):
        aux=datos.split(',',12)
        aux2=str(aux[5])
        aux3=str(aux[6])
        
        if(aux2!=usu and aux3 != contra):
            archivo2.write(datos)
        else:
            nuevo_usu = input("Ingrese nuevo numero de usuario: ")
            existe = veri(nuevo_usu)
            while(existe):
                    print("\nERROR\nUsuario ya existente\n")
                    nuevo_usu = input("Ingrese nuevo numero de usuario: ")
                    existe = veri(nuevo_usu)
            nueva_contra = input("Ingrese su nuevo numero de contraseña : ")
            cont += 1
            aux[5]= nuevo_usu
            aux[6]= nueva_contra
            aux = str(aux[0])+","+str(aux[1])+","+str(aux[2])+","+str(aux[3])+","+str(aux[4])+","+str(aux[5])+","+str(aux[6])+","+str(aux[7])+","+str(aux[8])+","+str(aux[9])
            archivo2.write(aux)
        datos=archivo.readline()
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
    print("\nVuelva a iniciar sesion\n")
    login()
def veri(usu):
    archivo=open("cliente_sube.txt","a")
    archivo.close()
    archivo=open("cliente_sube.txt","r")
    datos=archivo.readline()

    while (datos!=""):
        aux=datos.split(",",10)
        if (str(aux[5]) == str(usu)):
            return(True)
        datos=archivo.readline()
def menu(usu,contra):
    opc=int(input("1)Mostrar Saldo.\n2)Carga de Saldo.\n3)Movimientos del Usuario.\n4)Cobro.\n5)Modificar.\n6)Salir\n\n"))
    if(opc == 1):
        mostrar(usu,contra)
    if(opc == 2):
        carga_saldo(usu,contra)
    if(opc == 3):
        movimientos(usu,contra)
    if(opc == 4):
        print("\n")
        a=seleccion_linea()
        cobro(a,usu,contra)
    if(opc == 5):
        modifica(usu,contra)
    if(opc == 6):
        print("chao")
login()
