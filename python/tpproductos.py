#Ev_algoritmos_20230628
#---CARGA PRODUCTOS---------------------------------------------------------------------------------------------------
def cargar(productos,stock,precio):
    validacion=True
    print("¿Quieres agregar?")
    opcion=int(input("1)Si.\n2)No\n"))
    while(opcion!=1 and opcion!=2):
        print("-"*50)
        print("Intente elegir dentro de las opciones establecidas")
        print("-"*50)
        print("¿Quieres agregar?")
        opcion=int(input("1)Si.\n2)No\n"))
    if(opcion==1):
        contador=0
        for i in range(len(productos)):
            if(productos[i]==None):
                contador+=1
        nuevo=input("Ingrese nuevo producto: ")
        productos[len(productos)-contador]=nuevo.upper()
        nuevo_stock=int(input("Ingrese el nuevo stock: "))
        while(nuevo_stock<0): 
            print("No puede ser menor a 0")
            nuevo_stock=int(input("Ingrese el nuevo stock: "))
        stock[len(productos)-contador]=nuevo_stock
        nuevo_precio=float(input("Ingrese el nuevo precio: "))
        while(nuevo_precio<0):
            print("No puede ser menor a 0")
            nuevo_precio=float(input("Ingrese el nuevo precio: "))
        precio[len(productos)-contador]=nuevo_precio
        print("-"*50)
        menu(productos,stock,precio)
        
    elif(opcion==2):
        menu(productos,stock,precio)
#----MOSTRAR PRODUCTOS------------------------------------------------------------------------------------------------------
def mostrar(productos,stock,precio):
    print("¿Que desea hacer?")
    opcion=int(input("1)Mostrar Montos.\n2)Mostrar productos con menos de 200 unidades de stock.\n3)Mostrar de forma descendente\n4)Monto parcial y Monto total\n"))
    while(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4):
        print("-"*50)
        print("Intente elegir dentro de las opciones establecidas")
        print("-"*50)
        opcion=int(input("\n1)Mostrar Montos.\n2)Mostrar productos con menos de 200 unidades de stock.\n3)Mostrar de forma descendente\n4)Monto parcial y Monto total\n"))
    if(opcion==1):
        for i in range(len(productos)):
            if(productos[i]!=None):
                print("Producto",productos[i],"Stock",stock[i],"Precio",precio[i])

    elif(opcion==2):
        for i in range(len(productos)):
            if(productos[i]!=None and stock[i]<200):
                print("Producto",productos[i],"Stock",stock[i],"Precio",precio[i])

    elif(opcion==3):
        for i in range(len(productos)-1):
            for j in range(i+1,len(productos)):
                if(productos[i]!=None and productos[j]!=None):
                    if(productos[i]<productos[j]):
                        aux=productos[i]
                        productos[i]=productos[j]
                        productos[j]=aux
        for i in range(len(productos)):
            if(productos[i]!=None):
                print("Producto",productos[i],"Stock",stock[i],"Precio",precio[i])
        
    elif(opcion==4):
        monto_total=0
        for i in range(len(productos)):
            if(productos[i]!=None):
                monto_parcial=float(stock[i]*precio[i])
                monto_total+=monto_parcial
                print("EL monto parcial  de",productos[i],"es",monto_parcial)
            else:
                print()
        print("El monto total de todos los procutos es",monto_total)
    print("-"*50)
    menu(productos,stock,precio)
#---MODIFICAR PRODUCTOS------------------------------------------------------------------------------------
def modificar(productos,stock,precio):
    validacion=False
    seleccion=input("Ingrese producto a modificar: ")
    for i in range(len(productos)):
        if(productos[i]==seleccion.upper()):
            validacion=True
            print("Producto encontrado")
            nuevo_stock=int(input("Ingrese el nuevo stock: "))
            while(nuevo_stock<0): 
                print("No puede ser menor a 0")
                nuevo_stock=int(input("Ingrese el nuevo stock: "))
            stock[i]=nuevo_stock
            nuevo_precio=float(input("Ingrese el nuevo precio: "))
            while(nuevo_precio<0):
                print("No puede ser menor a 0")
                nuevo_precio=float(input("Ingrese el nuevo precio: "))
            precio[i]=nuevo_precio
        
    if(validacion):
        print("Cambio realizado")
    else:
        print("-"*50)
        print("Producto no encontrado")
    print("-"*50)
    menu(productos,stock,precio)
#---BUSCA PRODUCTOS---------------------------------------------------------------------------------------------------
def busca(productos,stock,precio):
    validacion=False
    seleccion=input("Ingrese producto a buscar: ")
    for i in range(len(productos)):
        if(productos[i]==seleccion.upper()):
            validacion=True
            print("Producto encontrado")
            print("Producto",productos[i],"Stock",stock[i],"Precio",precio[i])
    print("-"*50)
    if(validacion):
            print()
    else:
        print("Producto no encontrado")
    print("-"*50)
    menu(productos,stock,precio)
#---MENU--------------------------------------------------------------------------------------------------------------------------    
def menu(productos,stock,precio):
    print("Bienvenido")
    print("¿Que desea hacer?")
    opcion=int(input("1)Cargar productos.\n2)Mostrar los productos.\n3)Modificar.\n4)Buscar producto.\n5)Salir.\n"))
    while(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5):
        print("-"*50)
        print("Intente elegir dentro de las opciones establecidas")
        print("-"*50)
        opcion=int(input("1)Cargar productos.\n2)Mostrar los productos.\n3)Modificar.\n4)Buscar producto.\n5)Salir.\n"))
    if(opcion==1):
        cargar(productos,stock,precio)
    elif(opcion==2):
        mostrar(productos,stock,precio)
    elif(opcion==3):
        modificar(productos,stock,precio)
    elif(opcion==4):
        busca(productos,stock,precio)
    else:
        print("Chao")
        
#---PROGRAMA PRINCIPAL------------------------------------------------------------------------------------------------------------------------------------------
productos=["AAAA","AAAB","AAAC","AAAD","AAAE","AAAF","AAAG","AAAH","AAAI","AAAJ","AAAK","AAAL","AAAM","AAAN","AAAÑ","AAAO","AAAP","AAAQ","AAAR","AAAS","AAAT","AAAU","AAAV",
"AAAX","AAAY","AAAZ","AABB","AACC","AADD","AAEE","AAFF","AAGG","AAHH","AAII","AAJJ","AAKK","AALL","AAMM","AANN","AAÑÑ","AAOO","AAPP","AAQQ","AARR","AASS","AATT","AAUU","AAVV",
"AAWW","AAXX","AAYY","AAZZ","ABBB",None,None,None,None,None,None,None]

stock=[397, 268, 434, 409, 425, 943, 893, 413, 482, 969, 873, 929, 580, 618, 118, 346, 912, 857, 729, 833, 624, 579, 819, 211, 403, 38, 185, 907, 449, 904, 982, 68, 482, 684, 489, 470, 868, 530, 420, 387, 231, 47, 589, 704, 653, 655, 694, 968, 725, 423, 807, 922, 728,None,None,None,None,None,None,None]

precio=[1822.25, 180.89, 1662.85, 1477.22, 878.76, 790.14, 1141.2, 1936.94, 998.14, 1114.73, 1773.86, 1505.73, 1855.88, 1810.78, 607.65, 1280.61, 1631.55, 1493.54, 1523.93, 1462.11, 257.86, 1726.9, 1322.67, 1089.47, 1945.64, 1899.0, 1444.63, 990.78, 1675.68, 1210.0, 1735.22, 517.35, 1685.97, 267.78, 229.86, 1432.5, 1318.91, 571.35, 333.09, 1578.44, 601.97, 1094.23, 542.23, 1763.27, 1020.18, 110.83, 638.1, 988.69, 860.5, 141.61, 759.55, 964.07, 614.19,None,None,None,None,None,None,None]
menu(productos,stock,precio)
