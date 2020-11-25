
#ESTE PROGRAMA BUSCAR Y COMPARA PALABRAS DE UN ARCHIVO TIPO TEXTO (donde se describe Licencias)
#EN ARCHIVOS SIN EXTENSIÓN CON VARIOS TEXTOS QUE ESTÁN EN SUB CARPETAS
#SIMULA EL COMANDO GREP -GNU/LINUX
#Graba en CSV
import sys
import os
import pathlib

list_words = []
list_lines = []
#Activar la siguiente linea si desea grabar la salida de la terminal a un archivo de texto (colocar un correcto path)
sys.stdout =open("/home/sergioml/Documentos/Python/script/salida.csv", 'wt') # graba a u archivo de texto la salida.
#Colocar en la siguiente linea el path donde ponga la lista de licencias
f1 = open('/home/sergioml/Documentos/Python/script/licencias.txt',encoding= 'ISO 8859-1') #lista de licencias


for line in f1.readlines():
    # remove the trailing \n
    list_words.append(line[:-1])   #pabras se almacenan en una lista

salida=0
#Colocar el path donde haya desempaquetado la informacion de licencias
ejemplo_dir ='/home/sergioml/Documentos/Python/00'

directorio = pathlib.Path(ejemplo_dir)
ficheros = [fichero.name for fichero in directorio.iterdir() if fichero.is_dir()]
#print ("CARPETAS EXISTENTES")
numero= str(len(ficheros))
#print ('Existen:'+ numero + ' y son:')
#print (ficheros)
for x in range(0,len(ficheros)):
    carpeta=ficheros[x]
    #print ("Carpeta: "+carpeta)
    #Colocar el path donde haya desempaquetado la informacion de licencias
    search_path='/home/sergioml/Documentos/Python/00/'+ carpeta+'/'
    # Repite para cada archivo en el directorio
    for fname in os.listdir(path=search_path):
        # Apply file type filter    -> Aplicar filtro de tipo de archivo

            f2 = open(search_path + fname, encoding="ISO-8859-1") # pone a texto  actual en una lista
            salida=0
            bandera=1
            for line in f2.readlines():
            # remove the trailing \n
                list_lines.append(line[:-1])
                salida += 1#numero de lineas leidas

                for word in list_words:  #BUSCA PALABRAS RECORRE Y PREGUNTA
                    if word in line:
                        index = line.find(word)
                        #print(fname," --> ", line, sep=" ")
                        if(bandera==1):
                            print(carpeta,",",fname,",", word, sep=" ")
			    #print(fname)
			    #print(word)
                            bandera+=1
                    f2.close()
            salida2=str(salida)
            #print ('Lineas leidas en este texto:', salida2)

    f1.close()
#print (salida) #numero de lineas leidas restar -1  ----> no funciona al momento
