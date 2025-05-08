#Trenes
def crear_archivos():
    archivo= open ("Trenes.txt","w")
    linea_San_Martin="1"+" , "+"Linea SAN MARTIN"+" , "+"1"+" , "+"Ramal Retiro - Dr Cabred"+" , "+"Retiro"+" , "+"Palermo"+" , "+"Villa Crespo"+" , "+"La Paternal"+" , "+"Villa del Parque"+" , "+"Devoto"+" , "+"Sáenz Peña"+" , "+"Santos Lugares"+" , "+"Caseros"+" , "+"El Palomar"+" , "+"Hurlingham"+" , "+"William Morris"+" , "+"Bella Vista"+" , "+"Muñiz"+" , "+"San Miguel"+" , "+"José C. Paz"+" , "+"Sol y Verde"+" , "+"Derqui"+" , "+"Villa Astolfi"+" , "+"Pilar"+" , "+"Manzanares"+" , "+"Doctor Cabred "+"\n"
    linea_urquiza="2"+" , "+"Linea URQUIZA"+" , "+"1"+" , "+" Ramal FEDERICO LACROZE - General Lemos"+" , "+"Federico Lacroze"+" , "+"Artigas"+" , "+"Arata"+" , "+"Francisco Beiró"+" , "+"El Libertador"+" , "+"Devoto"+" , "+"Lynch"+" , "+"F. Moreno"+" , "+"Lourdes"+" , "+"Tropezón"+" , "+"J.M. Bosch"+" , "+"Martín Coronado"+" , "+"Pablo Podestá"+" , "+"Jorge Newbery"+" , "+"Rubén Darío"+" , "+"Ejército de los Andes"+" , "+"Lasalle"+" , "+"Sargento Barrufaldi"+" , "+"Capitán Lozano"+" , "+"Teniente Agneta"+" , "+"Campo de Mayo"+" , "+"Sargento Cabral"+" , "+"General Lemos"+"\n"
    linea_mitre_1_ramal="3"+" , "+"Linea MITRE"+" , "+"1"+" , "+" Ramal RETIRO - TIGRE"+" , "+"Retiro"+" , "+"Lisandro de la Torre"+" , "+"Belgrano C"+" , "+"Núñez"+" , "+"Rivadavia"+" , "+"Vicente López"+" , "+"Olivos"+" , "+"La Lucila"+" , "+"Martínez"+" , "+"Acassuso"+" , "+"San Isidro"+" , "+"Beccar"+" , "+"Victoria"+" , "+"Virreyes"+" , "+"San Fernando"+" , "+"Carupá"+" , "+"Tigre"+"\n"
    linea_mitre_2_ramal="3"+" , "+"Linea MITRE"+" , "+"2"+" , "+" Ramal RETIRO - J.L.Suarez"+" , "+"Retiro"+" , "+"Tres de Febrero"+" , "+"Carranza"+" , "+"Colegiales"+" , "+"Belgrano R"+" , "+"Drago"+" , "+"Urquiza"+" , "+"Pueyrredón"+" , "+"Miguelete"+" , "+"San Martín"+" , "+"San Andrés"+" , "+"Malaver"+" , "+"Villa Ballester"+" , "+"Chilavert"+" , "+"J. L. Suárez"+"\n"
    linea_mitre_3_ramal="3"+" , "+"Linea MITRE"+" , "+"3"+" , "+" Ramal RETIRO - MITRE"+" , "+"Retiro"+" , "+"Tres de Febrero"+" , "+"Carranza"+" , "+"Colegiales"+" , "+"Belgrano R"+" , "+"Coghland"+" , "+"Saavedra"+" , "+"Juan B. Justo"+" , "+"Florida"+" , "+"Dr. Centrangolo"+" , "+"Mitre"+"\n"
    linea_belgrano_norte="4"+" , "+"Linea BELGRANO NORTE"+" , "+"1"+" , "+" Ramal RETIRO - Villa Rosa"+" , "+"Retiro"+" , "+"Saldias"+" , "+"R.S. Ortiz"+" , "+"A. Del Valle"+" , "+"M.M. Padilla"+" , "+"FLorida"+" , "+"Munro"+" , "+"Carapachay"+" , "+"Villa Adelina"+" , "+"Boulogne Sur Mer"+" , "+"Vice A. Montes"+" , "+"Don Torcuato"+" , "+"A. Sourdeaux"+" , "+"Villa de mayo"+" , "+"Los polvorines"+" , "+"Ing. P. Nogues"+" , "+"Grand Bourg"+" , "+"Tierras Altas"+" , "+"Tortuguitas"+" , "+"Manuel Alberti"+" , "+"Del Viso"+" , "+"Villa Rosa"+"\n"
    linea_belgrano_sur_1_ramal="5"+" , "+"Linea BELGRANO SUR"+" , "+"1"+" , "+" Ramal CONSTITUCION - GONZALEz CATAN"+" , "+"Constitucion"+" , "+"Buenos Aires"+" , "+"Dr. Saenz"+" , "+"V. Soldati"+" , "+"PTE. ILLIA"+" , "+"V. LUGANO"+" , "+"V. MADERO"+" , "+"M. DEL FOURNIER"+" , "+"TAPIALES"+" , "+"ING. CASTELLO"+" , "+"KM 12"+" , "+"QUERANDI"+" , "+"LAFERRERE"+" , "+"EVA DUARTE"+" , "+"INDEPENDENCIA"+" , "+"GONZALES CATAN"+"\n"
    linea_belgrano_sur_2_ramal="5"+" , "+"Linea BELGRANO SUR"+" , "+"2"+" , "+" Ramal  Constitución - Marineros Crucero grl Belgrano"+" , "+"constitucion"+" , "+"Buenos aires"+" , "+"DR. SAENZ"+" , "+"V. SOLDATI"+" , "+"PTE. ILLIA"+" , "+"V. LUGANO"+" , "+"V. MADERO"+" , "+"M. DEL FOURNIER"+" , "+"TAPIALES"+" , "+"BONZI"+" , "+"M.S. MENDEVILLE"+" , "+"J. INGENIEROS"+" , "+"J. VILLEGAS"+" , "+"I. CASANOVA"+" , "+"R. CASTILLO"+" , "+"MERLO GOMEZ"+" , "+"LIBERTAD"+" , "+"MARINOS DEL CORONEL GNR BELGRANO"+"\n"
    linea_Sarmiento="6"+" , "+"Linea SARMIEnTO"+" , "+"1"+" , "+" Ramal  ONCE - Moreno"+" , "+"Once"+" , "+"Caballito"+" , "+"Flores"+" , "+"Floresta"+" , "+"Villa Luro"+" , "+"Liniers"+" , "+"Ciudadela"+" , "+"Ramos Mejía"+" , "+"Haedo"+" , "+"Morón"+" , "+"Castelar"+" , "+"Ituzaingó"+" , "+"San Antonio de Padua"+" , "+"Merlo"+" , "+"Paso del Rey"+" , "+"Moreno"+"\n"
    linea_roca_1_ramal="7"+" , "+"Linea roca"+" , "+"1"+" , "+" Ramal  Constitucion - la plata"+" , "+"Plaza Constitución"+" , "+"Sarandí"+" , "+"Villa Domínico"+" , "+"Wilde"+" , "+"Don Bosco"+" , "+"Bernal"+" , "+"Quilmes"+" , "+"Ezpeleta"+" , "+"Berazategui"+" , "+"Plátanos"+" , "+"Hudson"+" , "+"Pereyra"+" , "+"Villa Elisa"+" , "+"City Bell"+" , "+"Gonnet"+" , "+"Ringuelet"+" , "+"Tolosa"+" , "+"La Plata"+"\n"
    linea_roca_2_ramal="7"+" , "+"Linea roca"+" , "+"2"+" , "+" Ramal  Constitucion - BOSQUES"+" , "+"Plaza Constitución"+" , "+"Sarandí"+" , "+"Villa Domínico"+" , "+"Wilde"+" , "+"Don Bosco"+" , "+"Bernal"+" , "+"Quilmes"+" , "+"Ezpeleta"+" , "+"Berazategui"+" , "+"Villa España"+" , "+"Ranelagh"+" , "+"Sourigues"+" , "+"Bosques"+"\n"
    linea_roca_3_ramal="7"+" , "+"Linea roca"+" , "+"3"+" , "+" Ramal  EZEIZA - CAÑUELAS"+" , "+"Ezeiza"+" , "+"Unión Ferroviaria"+" , "+"Tristán Suárez"+" , "+"Spegazzini"+" , "+"Máximo Paz"+" , "+"Casares"+" , "+"Petión"+" , "+"Kloosterman"+" , "+"Levene"+" , "+"Cañuelas"+"\n"
   
    archivo.write(linea_San_Martin.upper())
    archivo.write(linea_urquiza.upper())
    archivo.write(linea_mitre_1_ramal.upper())
    archivo.write(linea_mitre_2_ramal.upper())
    archivo.write(linea_mitre_3_ramal.upper())
    archivo.write(linea_belgrano_norte.upper())
    archivo.write(linea_belgrano_sur_1_ramal.upper())
    archivo.write(linea_belgrano_sur_2_ramal.upper())
    archivo.write(linea_Sarmiento.upper())
    archivo.write(linea_roca_1_ramal.upper())
    archivo.write(linea_roca_2_ramal.upper())
    archivo.write(linea_roca_3_ramal.upper())
    archivo.close()

def seleccion_linea():
    crear_archivos()
    suma=float(7.5)
    costo_min=float(17.5)
    costo=float(90)
    opcion=int(input("1)Linea San Martin.\n2)Linea Urquiza.\n3)Linea Mitre.\n4)Linea Belgrano Norte.\n5)Linea Belgrano Sur.\n6)Linea Sarmiento.\n7)Linea Roca.\n8)Salir\n\n"))
    if(opcion==8):
        print("chao")
    if(opcion==1):
        opcion-=1
        a=seleccione_estacion(opcion,suma,costo_min,costo)
    if(opcion==2):
        opcion-=1
        a=seleccione_estacion(opcion,suma,costo_min,costo)
    if(opcion==3):
        ramal=int(input("1)Ramal RETIRO - TIGRE.\n2)Ramal RETIRO - J.L. Suarez.\n3)Ramal RETIRO - MITRE.\n4)Volver.\n\n"))
        if(ramal==4):
            seleccion_linea()
        if(ramal==1):
            ramal+=1
            a=seleccione_estacion(ramal,suma,costo_min,costo)
        if(ramal==2):
            ramal+=1
            a=seleccione_estacion(ramal,suma,costo_min,costo)
        if(ramal==3):
            ramal+=1
            a=seleccione_estacion(ramal,suma,costo_min,costo)        
    if(opcion==4):
        opcion+=1
        a=seleccione_estacion(opcion,suma,costo_min,costo)
    if(opcion==5):
        ramal2=int(input("1)Ramal CONSTITUCION - GONZALEZ CATAN.\n2)Ramal CONSTITUCION - MARINEROS CRUCERO GRL BELGRANO.\n3)Volver.\n\n"))
        if(ramal2==3):
            seleccion_linea()
        if(ramal2==1):
            ramal2+=5
            a=seleccione_estacion(ramal2,suma,costo_min,costo)
        if(ramal2==2):
            ramal2+=6
            a=seleccione_estacion(ramal2,suma,costo_min,costo)
    if(opcion==6):
        opcion+=2
        a=seleccione_estacion(opcion,suma,costo_min,costo)
    if(opcion==7):
        ramal3=int(input("1)Ramal CONSTITUCION - LA PLATA.\n2)Ramal CONSTITUCION - BOSQUES.\n3)Ramal EZEIZA - CAÑUELAS.\n4)Volver.\n\n"))
        if(ramal3==4):
            seleccion_linea()
        if(ramal3==1):
            ramal3+=8
            a=seleccione_estacion(ramal3,suma,costo_min,costo)
        if(ramal3==2):
            ramal3+=8
            a=seleccione_estacion(ramal3,suma,costo_min,costo)
        if(ramal3==3):
            ramal3+=8
            a=seleccione_estacion(ramal3,suma,costo_min,costo)
            
       
    return(a)
def precio(op,op2,linea,suma,costo_min,costo):
    cont=0
    archivo = open ("Trenes.txt","r")
    lee= archivo.readlines()
    aux=lee[linea].split(" , ",30)
    for i in range(4,len(aux)):

        if(i-3==op):
            nombre1=aux[i]
        if(i-3==op2):
            nombre2=aux[i]
    
    if(op2 > op):
        for i in range(op,op2):
            cont+=1
            if(cont<5):
                costo=costo_min
            elif(cont%5==0):
                costo+=suma
            

    if(op > op2):
        for i in range(op2,op):
            cont+=1
            if(cont<5):
                costo=costo_min
            elif(cont%5==0):
                costo+=suma
            
    print("-"*50)
    print("Su viaje es desde",nombre1," hasta ",nombre2)
    print("El costo de su viaje es de",costo)
    print("-"*50)
    print("\n")
    return(linea,costo,nombre1,nombre2)
def seleccione_estacion(linea,suma,costo_min,costo):
    print("--------------------------------------------------------------------------------")
    print()
    archivo = open ("Trenes.txt","r")
    lee= archivo.readlines()
    aux=lee[linea].split(" , ",30)
    print("                 "+aux[1]+" "+aux[3])
    for i in range(4,len(aux)):
        print(str(i-3)+")",aux[i])
    opcion=int(input("Seleccione estacion de inicio: "))

    print("\n")
    while(opcion >= len(aux) or opcion <= 0):
        print("ERROR SELECCIONE OTRA ESTACION")
        print()
        opcion=int(input("Seleccione estacion de inicio: "))
        print()
    print("--------------------------------------------------------------------------------")
    print()
    print("                 "+aux[1]+" "+aux[3])
    for i in range(4,len(aux)):
        if((i-3)!=opcion):
            print(str(i-3)+")",aux[i])
    opcion2 = int(input("Seleccione estacion de de fin: "))
    print("\n")
    while(opcion2 >= len(aux) or opcion2 <= 0 or opcion2==opcion):
        print("ERROR SELECCIONE OTRA ESTACION")
        print()
        opcion2=int(input("Seleccione estacion de fin: "))
        print()
 
    a=precio(opcion,opcion2,linea,suma,costo_min,costo)
    return(a)
