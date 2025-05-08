from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import tkinter
#Ventana_principal
vent1=Tk()
vent1.geometry('400x400')
vent1.title('Gestion')
#funciones
def alta():
    v_cursos=['',1,2,3,4,5,6]
    v_div=['',1,2,3,4,5,6,7,8,9]
    vent2=Tk()
    vent2.geometry('400x400')
    vent2.title('Alta')
    id=Label(vent2,text='Id del Alumno:')
    id.place(x=30,y=0,height=30,width=100)
    contador=open('contador.txt','a')
    contador.close()
    contador=open('contador.txt','r')
    a=str(contador.readline())
    if(a==''):
        a=0
    else:
        a=int(a)
    b=a+1
    id=Label(vent2,text=str(b))
    id.place(x=150,y=0,height=30,width=100)

    d=Label(vent2,text='DNI:')
    d.place(x=30,y=40,height=30,width=70)
    dni=Entry(vent2)
    dni.place(x=150,y=40,height=30,width=200)

    ape=Label(vent2,text='Apellido:')
    ape.place(x=30,y=80,height=30,width=70)
    apellido=Entry(vent2)
    apellido.place(x=150,y=80,height=30,width=200)

    nom=Label(vent2,text='Nombre:')
    nom.place(x=30,y=120,height=30,width=70)
    nombre=Entry(vent2)
    nombre.place(x=150,y=120,height=30,width=200)

    ema=Label(vent2,text='Email:')
    ema.place(x=30,y=160,height=30,width=70)
    email=Entry(vent2)
    email.place(x=150,y=160,height=30,width=200)

    curso=Label(vent2,text='Curso:')
    curso.place(x=30,y=200,height=30,width=70)
    curso_cmb=ttk.Combobox(vent2,state='readonly')
    curso_cmb['values']=v_cursos
    curso_cmb.place(x=150,y=200)

    division=Label(vent2,text='Division:')
    division.place(x=30,y=240,height=30,width=70)
    div_cmb=ttk.Combobox(vent2,state='readonly')
    div_cmb['values']=v_div
    div_cmb.place(x=150,y=240)

    bn1=Button(vent2,text='Ingresar',command=partial(ing_datos,nombre,apellido,dni,div_cmb,curso_cmb,email,v_cursos,v_div,vent2))
    bn1.place(x=150,y=280,height=30,width=70)
    bn2=Button(vent2,text='Volver',command=vent2.destroy)
    bn2.place(x=250,y=280,height=30,width=70)
def ing_datos(nombre,apellido,dni,div_cmb,curso_cmb,email,v_cursos,v_div,vent2):
    nombre1=str(nombre.get().capitalize())
    apellido1=str(apellido.get().upper())
    dni1=str(dni.get())
    div1=str(div_cmb.get())
    curso1=str(curso_cmb.get())
    email1=str(email.get().lower())
    nombre.delete(0,END)
    apellido.delete(0,END)
    dni.delete(0,END)
    email.delete(0,END)
    div_cmb.set(v_div[0])
    curso_cmb.set(v_cursos[0])
    if(len(nombre1)>0 and len(apellido1)>0 and len(dni1)>0 and len(div1)>0 and len(curso1)>0 and len(email1)>0):
        if(verificar(email1)):
            contador=open('contador.txt','a')
            contador.close()
            contador=open('contador.txt','r')
            a=str(contador.readline())
            if(a==''):
                a=0
            else:
                a=int(a)
            b=a+1
            notas=open('cursos_alumnos.txt','a')
            notas.close()
            arch=open('cursos_alumnos.txt','a')
            auxiliar=str(b)+', '+curso1+'\n'
            arch.write(auxiliar)
            arch.close()
            cc=Label(vent2,text=str(int(b+1)))
            cc.place(x=150,y=0,height=30,width=100)
            contador=open('contador.txt','w')
            contador.write(str(b))
            contador.close()
            archivo=open('gestion.txt','a')
            datos_aux=str(b)+' , '+dni1+' , '+apellido1+' , '+nombre1+' , '+email1+' , '+curso1+' , '+div1+'\n'
            archivo.write(str(datos_aux))
            archivo.close()
        else:
            messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def verificar(email1):
    cont=int(0)
    posi=int(0)
    for i in range(len(email1)):
        if(email1[i]=='@'):
            cont+=1
            posi=i-1
    if(cont==1):
        for m in range(posi,len(email1)):
            if(email1[m]== '.'):
                return(True)
    else:
        return(False)

def Baja():
    vent4=Tk()
    vent4.geometry('400x400')
    vent4.title('Baja de Datos')
    a=Label(vent4,text='Id del alumno a eliminar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent4)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent4,text='Ingresar',command=partial(bajado,b,vent4))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent4,text='Volver',command=vent4.destroy)
    bn2.place(x=290,y=50,height=30,width=70)
def bajado(b,vent4):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion.txt','r')
        archivo_temp=open('gestion_baja.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            print(aux[0])
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion.txt','w')
        archivo_temp=open('gestion_baja.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()

        archivo_datos=open('gestion_notas.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_notas.txt','r')
        archivo_temp=open('gestion_baja_notas.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            print(aux[0])
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion_notas.txt','w')
        archivo_temp=open('gestion_baja_notas.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()
        
   
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos',parent=(vent4))
def modifica():
    vent5=Tk()
    vent5.geometry('400x400')
    vent5.title('Modificacion de Datos')
    a=Label(vent5,text='Id del alumno a modificar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent5)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent5,text='Ingresar',command=partial(modificando,b,vent5))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent5,text='Volver',command=vent5.destroy)
    bn2.place(x=290,y=50,height=30,width=70)
def modificando(b,vent5):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion.txt','r')
        archivo_temp=open('gestion_moficia.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            aux2=int(aux[0])
            if(aux2==en):
                messagebox.showinfo(title='Correcto',message='El alumno fue encontrado',parent=(vent5))
                modificao(en)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos',parent=(vent5))
               
def modificao(en):
    archivo_datos=open('gestion.txt','a')
    archivo_datos.close()
    archivo_datos=open('gestion.txt','r')
    archivo_temp=open('gestion_moficia.txt','w')
    datos=archivo_datos.readline()
    while(datos!=''):
        aux=datos.split(',',7)
        aux2=int(aux[0])
       
        if(aux2!=en):
            archivo_temp.write(datos)
        else:
            v_cursos=['',1,2,3,4,5,6]
            v_div=['',1,2,3,4,5,6,7,8,9]
            vent2=Tk()
            vent2.geometry('400x400')
            vent2.title('Alta')
            id=Label(vent2,text='Id del Alumno:')
            id.place(x=30,y=0,height=30,width=100)
            contador=open('contador.txt','a')
            contador.close()
            contador=open('contador.txt','r')
            a=str(contador.readline())
            if(a==''):
                a=0
            else:
                a=int(a)
            b=a+1
            id=Label(vent2,text=str(en))
            id.place(x=150,y=0,height=30,width=100)

            d=Label(vent2,text='DNI:')
            d.place(x=30,y=40,height=30,width=70)
            dni=Entry(vent2)
            dni.place(x=150,y=40,height=30,width=200)

            ape=Label(vent2,text='Apellido:')
            ape.place(x=30,y=80,height=30,width=70)
            apellido=Entry(vent2)
            apellido.place(x=150,y=80,height=30,width=200)

            nom=Label(vent2,text='Nombre:')
            nom.place(x=30,y=120,height=30,width=70)
            nombre=Entry(vent2)
            nombre.place(x=150,y=120,height=30,width=200)

            ema=Label(vent2,text='Email:')
            ema.place(x=30,y=160,height=30,width=70)
            email=Entry(vent2)
            email.place(x=150,y=160,height=30,width=200)

            curso=Label(vent2,text='Curso:')
            curso.place(x=30,y=200,height=30,width=70)
            curso_cmb=ttk.Combobox(vent2,state='readonly')
            curso_cmb['values']=v_cursos
            curso_cmb.place(x=150,y=200)

            division=Label(vent2,text='Division:')
            division.place(x=30,y=240,height=30,width=70)
            div_cmb=ttk.Combobox(vent2,state='readonly')
            div_cmb['values']=v_div
            div_cmb.place(x=150,y=240)

            bn1=Button(vent2,text='Ingresar',command=partial(modi_archivo,ing_datos,nombre,apellido,dni,div_cmb,curso_cmb,email,v_cursos,v_div,vent2,en))
            bn1.place(x=150,y=280,height=30,width=70)
            bn2=Button(vent2,text='Volver',command=vent2.destroy)
            bn2.place(x=250,y=280,height=30,width=70)
        datos=archivo_datos.readline()        
    archivo_datos.close()
    archivo_temp.close()
def modi_archivo(ing_datos,nombre,apellido,dni,div_cmb,curso_cmb,email,v_cursos,v_div,vent2,en):
    nombre1=str(nombre.get().capitalize())
    apellido1=str(apellido.get().upper())
    dni1=str(dni.get())
    div1=str(div_cmb.get())
    curso1=str(curso_cmb.get())
    email1=str(email.get().lower())
    nombre.delete(0,END)
    apellido.delete(0,END)
    dni.delete(0,END)
    email.delete(0,END)
    div_cmb.set(v_div[0])
    curso_cmb.set(v_cursos[0])
    if(len(nombre1)>0 and len(apellido1)>0 and len(dni1)>0 and len(div1)>0 and len(curso1)>0 and len(email1)>0):
        if(verificar(email1)):
            notas=open('cursos_alumnos.txt','a')
            notas.close()
            arch=open('cursos_alumnos.txt','a')
            auxiliar=str(en)+', '+curso1+'\n'
            arch.write(auxiliar)
            arch.close()
            archivo_datos=open('gestion.txt','a')
            archivo_datos.close()
            archivo_datos=open('gestion.txt','r')
            archivo_temp=open('gestion_moficia.txt','w')
            datos=archivo_datos.readline()
            while(datos!=''):
                aux=datos.split(',',7)
                aux2=int(aux[0])
                if(aux2!=en):
                    archivo_temp.write(datos)
                else:
                    auxiliar=str(en)+' , '+dni1+' , '+apellido1+' , '+nombre1+' , '+email1+' , '+curso1+' , '+div1+'\n'
                    archivo_temp.write(auxiliar)
                datos=archivo_datos.readline()
            archivo_datos.close()
            archivo_temp.close()
            archivo_datos=open('gestion.txt','w')
            archivo_temp=open('gestion_moficia.txt','r')
            datos=archivo_temp.readline()
            while(datos!=''):
                archivo_datos.write(datos)
                datos=archivo_temp.readline()
            archivo_datos.close()
            archivo_temp.close()
           
        else:
            messagebox.showerror(title='ERROR',message='Error en ingreso de datos',parent=vent2)
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos',parent=vent2)
def verificar(email1):
    cont=int(0)
    posi=int(0)
    for i in range(len(email1)):
        if(email1[i]=='@'):
            cont+=1
            posi=i-1
    if(cont==1):
        for m in range(posi,len(email1)):
            if(email1[m]== '.'):
                return(True)
    else:
        return(False)

def lista():
    vent3 = Tk()
    vent3.title('Lista de datos')
    vent3.geometry('1400x700')
    columns = ('Id', 'DNI', 'Apellido','Nombre', 'Email', 'Curso','Division')
    tree = ttk.Treeview(vent3, columns=columns, show='headings')
    tree.heading('Id', text='Id')
    tree.heading('DNI', text='DNI')
    tree.heading('Apellido', text='Apellido')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Email', text='Email')
    tree.heading('Curso', text='Curso')
    tree.heading('Division', text='Division')
    tree.place(x=0,y=0,height=700,width=1400)
    tree.bind("<ButtonRelease-1>", lambda event, trv=tree:clicker(event, trv,vent3))
    archivo=open('gestion.txt','a')
    archivo.close()
    archivo_datos=open('gestion.txt','r')
    datos=archivo_datos.readline()
    while(datos!=''):
        aux=datos.split(',',7)
        tree.insert('',END,values=(aux))
        datos=archivo_datos.readline()
    archivo_datos.close()
def clicker(event,trv,vent3):
    elegido = trv.focus()
    tmp = trv.item(elegido, 'values')
    en=tmp[0]
    b=messagebox.askquestion(title="prueba", message="¿Quiere ver las notas",parent=vent3)
    if(b=='yes'):
        lista_notas()
def alta_notas():
    vent2=Tk()
    vent2.geometry('400x400')
    vent2.title('Alta de notas')
    id_nota=Label(vent2,text='Id de nota')
    id_nota.place(x=20,y=0,height=30,width=120)
    contador_n=open('contador_notas.txt','a')
    contador_n.close()
    contador=open('contador_notas.txt','r')
    n=str(contador.readline())
    if(n==''):
        n=0
    else:
        n=int(n)
    b=n+1
    
    id=Label(vent2,text=str(b))
    id.place(x=180,y=0,height=30,width=180)
    id_alu=Label(vent2,text='Apellidos')
    id_alu.place(x=20,y=30,height=30,width=120)
    archivo_ape=open('gestion.txt','a')
    archivo_ape.close()
    archivo_ape=open('gestion.txt','r')
    datos=archivo_ape.readline()
    vec=['']
    while(datos!=''):
        aux=datos.split(',',7)
        vec.append(aux[2])
        datos=archivo_ape.readline()     
    archivo_ape.close()
    
    apellido=ttk.Combobox(vent2,state='readonly')
    apellido['values']=vec
    apellido.place(x=180,y=30)

    id_mat=Label(vent2,text='Materias')
    id_mat.place(x=20,y=60,height=30,width=120)
    archivo_mat=open('gestion_materias.txt','a')
    archivo_mat.close()
    archivo_mat=open('gestion_materias.txt','r')
    datos2=archivo_mat.readline()
    vec_mat=['']
    while(datos2!=''):
        aux=datos2.split(',',7)
        vec_mat.append(aux[1])
        datos2=archivo_mat.readline()     
    archivo_mat.close()
    
    materias=ttk.Combobox(vent2,state='readonly')
    materias['values']=vec_mat
    materias.place(x=180,y=60)

    notas_1=['',1,2,3,4,5,6,7,8,9,10]
    label1=Label(vent2,text='Nota 1° bimestre')
    label1.place(x=20,y=90,height=30,width=120)
    label2=Label(vent2,text='Nota 2° bimestre')
    label2.place(x=20,y=120,height=30,width=120)
    label3=Label(vent2,text='Nota 3° bimestre')
    label3.place(x=20,y=150,height=30,width=120)
    label4=Label(vent2,text='Nota 4° bimestre')
    label4.place(x=20,y=180,height=30,width=120)
    no1=ttk.Combobox(vent2,state='readonly')
    no1['values']=notas_1
    no1.place(x=180,y=90)
    
    no2=ttk.Combobox(vent2,state='readonly')
    no2['values']=notas_1
    no2.place(x=180,y=120)

    no3=ttk.Combobox(vent2,state='readonly')
    no3['values']=notas_1
    no3.place(x=180,y=150)

    no4=ttk.Combobox(vent2,state='readonly')
    no4['values']=notas_1
    no4.place(x=180,y=180)

    btn1=Button(vent2,text='Ingresar',command=partial(alta_not,no1,no2,no3,no4,apellido,materias,vent2,vec,vec_mat,notas_1))
    btn1.place(x=180,y=210,height=30,width=70)
    btn2=Button(vent2,text='Volver',command=vent2.destroy)
    btn2.place(x=280,y=210,height=30,width=70)
    vent2.mainloop()
def alta_not(no1,no2,no3,no4,apellido,materias,vent2,vec,vec_mat,notas_1):
    nt1=str(no1.get())
    nt2=str(no2.get())
    nt3=str(no3.get())
    nt4=str(no4.get())
    nt5=str(apellido.get())
    nt6=str(materias.get())
    if(len(nt1)>0 and len(nt2)>0 and len(nt3)>0 and len(nt4)>0 and len(nt5)>0 and len(nt6)>0):
            no1.set(notas_1[0])
            no2.set(notas_1[0])
            no3.set(notas_1[0])
            no4.set(notas_1[0])
            apellido.set(vec[0])
            materias.set(vec[0])
            contador_n=open('contador_notas.txt','a')
            contador_n.close()
            contador=open('contador_notas.txt','r')
            n=str(contador.readline())
            if(n==''):
                n=0
            else:
                n=int(n)
            b=n+1
            contador.close()
            cc=Label(vent2,text=str(int(b+1)))
            cc.place(x=180,y=0,height=30,width=180)
            contador=open('contador_notas.txt','w')
            contador.write(str(b))
            contador.close()
            notas=open('gestion_notas.txt','a')
            aux=str(b)+' ,'+nt5+', '+nt6+', '+nt1+' ,'+nt2+' ,'+nt3+', '+nt4+'\n'
            notas.write(aux)
            notas.close()
    else:
            messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def baja_nota():
    vent4=Tk()
    vent4.geometry('400x400')
    vent4.title('Baja de Datos')
    a=Label(vent4,text='Id de notas a eliminar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent4)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent4,text='Ingresar',command=partial(bajado_nota,b))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent4,text='Volver',command=vent4.destroy)
    bn2.place(x=290,y=50,height=30,width=70)
def bajado_nota(b):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion_notas.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_notas.txt','r')
        archivo_temp=open('gestion_baja_notas.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            print(aux[0])
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion_notas.txt','w')
        archivo_temp=open('gestion_baja_notas.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()

        archivo_datos=open('gestion.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion.txt','r')
        archivo_temp=open('gestion_baja.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            print(aux[0])
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion.txt','w')
        archivo_temp=open('gestion_baja.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()
   
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def modifica_notas():
    vent5=Tk()
    vent5.geometry('400x400')
    vent5.title('Modificacion de Datos')
    a=Label(vent5,text='id de nota a modificar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent5)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent5,text='Ingresar',command=partial(modificando_notas,b,vent5))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent5,text='Volver',command=vent5.destroy)
    bn2.place(x=290,y=50,height=30,width=70)
def modificando_notas(b,vent5):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion_notas.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_notas.txt','r')
        archivo_temp=open('gestion_modifica_notas.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            aux2=int(aux[0])
            if(aux2==en):
                messagebox.showinfo(title='Correcto',message='El alumno fue encontrado')
                modificarr_notas(en)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def modificarr_notas(en):
    archivo_datos=open('gestion_notas.txt','a')
    archivo_datos.close()
    archivo_datos=open('gestion_notas.txt','r')
    archivo_temp=open('gestion_modifica_notas.txt','w')
    datos=archivo_datos.readline()
    while(datos!=''):
        aux=datos.split(',',7)
        aux2=int(aux[0])
        if(aux2!=en):
            archivo_temp.write(datos)
        else:
            vent2=Tk()
            vent2.geometry('400x400')
            vent2.title('Alta de notas')
            id_nota=Label(vent2,text='Id de nota')
            id_nota.place(x=20,y=0,height=30,width=120)
            contador_n=open('contador_notas.txt','a')
            contador_n.close()
            id=Label(vent2,text=str(en))
            id.place(x=180,y=0,height=30,width=180)
            id_alu=Label(vent2,text='Apellidos')
            id_alu.place(x=20,y=30,height=30,width=120)
            archivo_ape=open('gestion.txt','a')
            archivo_ape.close()
            archivo_ape=open('gestion.txt','r')
            datos=archivo_ape.readline()
            vec=['']
            while(datos!=''):
                aux=datos.split(',',7)
                vec.append(aux[2])
                datos=archivo_ape.readline()     
            archivo_ape.close()
            
            apellido=ttk.Combobox(vent2,state='readonly')
            apellido['values']=vec
            apellido.place(x=180,y=30)

            id_mat=Label(vent2,text='Materias')
            id_mat.place(x=20,y=60,height=30,width=120)
            archivo_mat=open('gestion_materias.txt','a')
            archivo_mat.close()
            archivo_mat=open('gestion_materias.txt','r')
            datos2=archivo_mat.readline()
            vec_mat=['']
            while(datos2!=''):
                aux=datos2.split(',',7)
                vec_mat.append(aux[1])
                datos2=archivo_mat.readline()     
            archivo_mat.close()
            
            materias=ttk.Combobox(vent2,state='readonly')
            materias['values']=vec_mat
            materias.place(x=180,y=60)

            notas_1=['',1,2,3,4,5,6,7,8,9,10]
            label1=Label(vent2,text='Nota 1° bimestre')
            label1.place(x=20,y=90,height=30,width=120)
            label2=Label(vent2,text='Nota 2° bimestre')
            label2.place(x=20,y=120,height=30,width=120)
            label3=Label(vent2,text='Nota 3° bimestre')
            label3.place(x=20,y=150,height=30,width=120)
            label4=Label(vent2,text='Nota 4° bimestre')
            label4.place(x=20,y=180,height=30,width=120)
            no1=ttk.Combobox(vent2,state='readonly')
            no1['values']=notas_1
            no1.place(x=180,y=90)
            
            no2=ttk.Combobox(vent2,state='readonly')
            no2['values']=notas_1
            no2.place(x=180,y=120)

            no3=ttk.Combobox(vent2,state='readonly')
            no3['values']=notas_1
            no3.place(x=180,y=150)

            no4=ttk.Combobox(vent2,state='readonly')
            no4['values']=notas_1
            no4.place(x=180,y=180)

            btn1=Button(vent2,text='Ingresar',command=partial(modifica_archivo_notas,no1,no2,no3,no4,apellido,materias,vent2,vec,vec_mat,notas_1,en))
            btn1.place(x=180,y=210,height=30,width=70)
            btn2=Button(vent2,text='Volver',command=vent2.destroy)
            btn2.place(x=280,y=210,height=30,width=70)
            vent2.mainloop()
        datos=archivo_datos.readline()
    archivo_datos.close()
    archivo_temp.close()
def modifica_archivo_notas(no1,no2,no3,no4,apellido,materias,vent2,vec,vec_mat,notas_1,en):
    nt1=str(no1.get())
    nt2=str(no2.get())
    nt3=str(no3.get())
    nt4=str(no4.get())
    nt5=str(apellido.get())
    nt6=str(materias.get())
    if(len(nt1)>0 and len(nt2)>0 and len(nt3)>0 and len(nt4)>0 and len(nt5)>0 and len(nt6)>0):
        no1.set(notas_1[0])
        no2.set(notas_1[0])
        no3.set(notas_1[0])
        no4.set(notas_1[0])
        apellido.set(vec[0])
        materias.set(vec_mat[0])
        archivo_datos=open('gestion_notas.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_notas.txt','r')
        archivo_temp=open('gestion_modifica_notas.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',7)
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            else:
                auxiliar=str(en)+' ,'+nt5+', '+nt6+', '+nt1+' ,'+nt2+' ,'+nt3+', '+nt4+'\n'
                archivo_temp.write(auxiliar)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion_notas.txt','w')
        archivo_temp=open('gestion_modifica_notas.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()

    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def lista_notas():
    vent3 = Tk()
    vent3.title('Lista de datos')
    vent3.geometry('1500x1500')
   
    columns = ('Id', 'id2', 'id3','Nota 1° Bimestre', 'Nota 2° Bimestre','Nota 3° Bimestre', 'Nota 4° Bimestre')
    tree = ttk.Treeview(vent3, columns=columns, show='headings')
    tree.heading('Id', text='Id de nota')
    tree.heading('id2', text='Apellido')
    tree.heading('id3', text='Materia')
    tree.heading('Nota 1° Bimestre', text='Nota 1° Bimestre')
    tree.heading('Nota 2° Bimestre', text='Nota 2° Bimestre')
    tree.heading('Nota 3° Bimestre', text='Nota 3° Bimestre')
    tree.heading('Nota 4° Bimestre', text='Nota 4° Bimestre')
    tree.place(x=0,y=0,height=1200,width=1500)
    archivo=open('gestion_notas.txt','a')
    archivo.close()
    archivo=open('gestion_notas.txt','r')
    datos=archivo.readline()
    while(datos!=''):
        aux=datos.split(',',7)
        tree.insert('',END,values=(aux))
        datos=archivo.readline()
    archivo.close()

    
def alta_materias():
    v_cursos=['',1,2,3,4,5,6]
    vent2=Tk()
    vent2.geometry('400x400')
    vent2.title('Alta de materias')
    id_nota=Label(vent2,text='Id de materias')
    id_nota.place(x=20,y=0,height=30,width=120)
    contador_n=open('contador_materias.txt','a')
    contador_n.close()
    contador=open('contador_materias.txt','r')
    n=str(contador.readline())
    if(n==''):
        n=0
    else:
        n=int(n)
    b=n+1
    id=Label(vent2,text=str(b))
    id.place(x=180,y=0,height=30,width=180)
    label1=Label(vent2,text='Nombre')
    label1.place(x=20,y=30,height=30,width=120)
    entry1=Entry(vent2)
    entry1.place(x=180,y=30,height=30,width=180)
    curso=Label(vent2,text='Curso:')
    curso.place(x=30,y=60,height=30,width=70)
    curso_cmb=ttk.Combobox(vent2,state='readonly')
    curso_cmb['values']=v_cursos
    curso_cmb.place(x=180,y=70)
    btn1=Button(vent2,text='Ingresar',command=partial(alta_mate,entry1,curso_cmb,vent2,v_cursos))
    btn1.place(x=180,y=200,height=30,width=70)
    btn2=Button(vent2,text='Volver',command=vent2.destroy)
    btn2.place(x=280,y=200,height=30,width=70)
    vent2.mainloop()
def alta_mate(entry1,curso_cmb,vent2,v_cursos):
    nt1=str(entry1.get().capitalize())
    nt2=str(curso_cmb.get())
    if(len(nt1)>0 and len(nt2)>0):
        entry1.delete(0,END)
        curso_cmb.set(v_cursos[0])
        contador_n=open('contador_materias.txt','a')
        contador_n.close()
        contador=open('contador_materias.txt','r')
        n=str(contador.readline())
        if(n==''):
            n=0
        else:
            n=int(n)
        b=n+1                                 
        cc=Label(vent2,text=str(int(b+1)))
        cc.place(x=180,y=0,height=30,width=180)
        contador=open('contador_materias.txt','w')
        contador.write(str(b))
        contador.close()
        notas=open('gestion_materias.txt','a')
        aux=str(b)+' ,'+nt1+', '+nt2+'\n'
        notas.write(aux)
        notas.close()
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def baja_materias():
    vent4=Tk()
    vent4.geometry('400x400')
    vent4.title('Baja de Datos')
    a=Label(vent4,text='Id de la materia a eliminar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent4)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent4,text='Ingresar',command=partial(bajado_materias,b))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent4,text='Volver',command=vent4.destroy)
    bn2.place(x=290,y=50,height=30,width=70)
def bajado_materias(b):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion_materias.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_materias.txt','r')
        archivo_temp=open('gestion_baja_materias.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',3)
            print(aux[0])
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion_materias.txt','w')
        archivo_temp=open('gestion_baja_materias.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()
   
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def modifica_materias():
    vent5=Tk()
    vent5.geometry('400x400')
    vent5.title('Modificacion de Datos')
    a=Label(vent5,text='id de la materia a modificar')
    a.place(x=0,y=0,height=30,width=180)
    b=Entry(vent5)
    b.place(x=180,y=0,height=30,width=200)
    bn1=Button(vent5,text='Ingresar',command=partial(modificando_materias,b,vent5))
    bn1.place(x=190,y=50,height=30,width=70)
    bn2=Button(vent5,text='Volver',command=vent5.destroy)
    bn2.place(x=290,y=50,height=30,width=70)

def modificando_materias(b,vent5):
    en=str(b.get())
    if(len(en)>0):
        en=int(en)
        b.delete(0,END)
        archivo_datos=open('gestion_materias.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_materias.txt','r')
        archivo_temp=open('gestion_modifica_materias.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',3)
            aux2=int(aux[0])
            if(aux2==en):
                messagebox.showinfo(title='Correcto',message='La Materia fue encontrado',parent=vent5)
                modificarr_materias(en)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos',parent=vent5)
def modificarr_materias(en):
    archivo_datos=open('gestion_materias.txt','a')
    archivo_datos.close()
    archivo_datos=open('gestion_materias.txt','r')
    archivo_temp=open('gestion_modifica_materias.txt','w')
    datos=archivo_datos.readline()
    while(datos!=''):
        aux=datos.split(',',3)
        aux2=int(aux[0])
        if(aux2!=en):
            archivo_temp.write(datos)
        else:
            v_cursos=['',1,2,3,4,5,6]
            vent2=Tk()
            vent2.geometry('400x400')
            vent2.title('Alta de materias')
            id_nota=Label(vent2,text='Id de materias')
            id_nota.place(x=20,y=0,height=30,width=120)
            contador_n=open('contador_materias.txt','a')
            contador_n.close()
            contador=open('contador_materias.txt','r')
            n=str(contador.readline())
            if(n==''):
                n=0
            else:
                n=int(n)
                b=n+1
            id=Label(vent2,text=str(en))
            id.place(x=180,y=0,height=30,width=180)
            materias=Label(vent2,text='Materias:')
            materias.place(x=30,y=60,height=30,width=70)
            
            label1=Label(vent2,text='Nombre')
            label1.place(x=20,y=30,height=30,width=120)
            entry1=Entry(vent2)
            entry1.place(x=180,y=30,height=30,width=180)
           
            curso=Label(vent2,text='Curso:')
            curso.place(x=30,y=60,height=30,width=70)
            
            curso_cmb=ttk.Combobox(vent2,state='readonly')
            curso_cmb['values']=v_cursos
            curso_cmb.place(x=180,y=70)
            btn1=Button(vent2,text='Ingresar',command=partial(modifica_archivo_materias,entry1,curso_cmb,vent2,en,v_cursos))
            btn1.place(x=180,y=200,height=30,width=70)
            btn2=Button(vent2,text='Volver',command=vent2.destroy)
            btn2.place(x=280,y=200,height=30,width=70)
            vent2.mainloop()
        datos=archivo_datos.readline()
    archivo_datos.close()
    archivo_temp.close()
def modifica_archivo_materias(entry1,curso_cmb,vent2,en,v_cursos):
    nt1=str(entry1.get())
    nt2=str(curso_cmb.get())
    if(len(nt1)>0 and len(nt2)>0):
        entry1.delete(0,END)
        curso_cmb.set(v_cursos[0])
        notas=open('cursos_materias.txt','a')
        notas.close()
        arch=open('cursos_materias.txt','a')
        auxiliar=nt1+', '+nt2+'\n'
        arch.write(auxiliar)
        arch.close()
        archivo_datos=open('gestion_materias.txt','a')
        archivo_datos.close()
        archivo_datos=open('gestion_materias.txt','r')
        archivo_temp=open('gestion_modifica_materias.txt','w')
        datos=archivo_datos.readline()
        while(datos!=''):
            aux=datos.split(',',3)
            aux2=int(aux[0])
            if(aux2!=en):
                archivo_temp.write(datos)
            else:
                auxiliar=str(en)+' ,'+nt1+', '+nt2+'\n'
                archivo_temp.write(auxiliar)
            datos=archivo_datos.readline()
        archivo_datos.close()
        archivo_temp.close()
        archivo_datos=open('gestion_materias.txt','w')
        archivo_temp=open('gestion_modifica_materias.txt','r')
        datos=archivo_temp.readline()
        while(datos!=''):
            archivo_datos.write(datos)
            datos=archivo_temp.readline()
        archivo_datos.close()
        archivo_temp.close()
    else:
        messagebox.showerror(title='ERROR',message='Error en ingreso de datos')
def lista_materias():
    vent3 = Tk()
    vent3.title('Lista de datos')
    vent3.geometry('700x700')
   
    columns = ('Id', 'Nombre', 'Curso')
    tree = ttk.Treeview(vent3, columns=columns, show='headings')
    tree.heading('Id', text='Id')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Curso', text='Curso')
    tree.place(x=0,y=0,height=700,width=700)
    
    archivo=open('gestion_materias.txt','a')
    archivo.close()
    archivo_datos=open('gestion_materias.txt','r')
    datos=archivo_datos.readline()
    while(datos!=''):
        aux=datos.split(',',3)
        tree.insert('',END,values=(aux))
        datos=archivo_datos.readline()
    archivo_datos.close()
#componentes
lb1=Label(vent1,text='Alumnos')
lb1.place(x=30,y=0,height=30,width=70)
bn1=Button(vent1,text='ALTA',command=partial(alta))
bn1.place(x=30,y=50,width=70,height=30)

bn2=Button(vent1,text='BAJA',command=partial(Baja))
bn2.place(x=30,y=100,width=70,height=30)

bn3=Button(vent1,text='MODIFICA',command=partial(modifica))
bn3.place(x=25,y=150,width=80,height=30)

bn4=Button(vent1,text='LISTA',command=partial(lista))
bn4.place(x=30,y=200,width=70,height=30)

lb2=Label(vent1,text='Notas')
lb2.place(x=310,y=0,height=30,width=70)
bn1_notas=Button(vent1,text='ALTA',command=partial(alta_notas))
bn1_notas.place(x=310,y=50,width=70,height=30)

bn2_notas=Button(vent1,text='BAJA',command=partial(baja_nota))
bn2_notas.place(x=310,y=100,width=70,height=30)

bn3_notas=Button(vent1,text='MODIFICA',command=partial(modifica_notas))
bn3_notas.place(x=305,y=150,width=80,height=30)

bn4_notas=Button(vent1,text='LISTA',command=partial(lista_notas))
bn4_notas.place(x=310,y=200,width=70,height=30)

lb3=Label(vent1,text='Materias')
lb3.place(x=180,y=0,height=30,width=70)
bn1_materias=Button(vent1,text='ALTA',command=partial(alta_materias))
bn1_materias.place(x=180,y=50,width=70,height=30)
bn2_materias=Button(vent1,text='BAJA',command=partial(baja_materias))
bn2_materias.place(x=180,y=100,width=70,height=30)
bn3_materias=Button(vent1,text='MODIFICA',command=partial(modifica_materias))
bn3_materias.place(x=175,y=150,width=80,height=30)
bn4_materias=Button(vent1,text='LISTA',command=partial(lista_materias))
bn4_materias.place(x=180,y=200,width=70,height=30)

vent1.mainloop()
