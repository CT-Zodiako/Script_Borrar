import os
import time


#Dirrecion de la carpeta
print('Escriba la ruta de su carpeta: ')
print('Ejemplo: D:\Descargas/ ')

path = (input())

print('Tiempo en dias de archivos que quieres eliminar ')
tiempo_eliminar=(int(input()))
tiempo= tiempo_eliminar*86400

#Renombro la funcion listdir
lista_Archivos = os.listdir(path)
number_files = (len(lista_Archivos))
rango = number_files


#Entra en un ciclo para poder hacer una lista con los nombres de los archivos
for Archivo in range(rango):
    lista_Archivos[Archivo]

#Renombro la lista 
lista = lista_Archivos

#En este ciclo compara las fecha actual con la fecha de creacion mas el tiempo que quieres que este en el pc
for i in range(len(lista)):
    fecha = os.path.getctime(path + lista[i])
    fecha_eliminar = fecha+tiempo #Tiempo unix
    if time.time() > fecha_eliminar:
        os.remove(path + lista[i])  


print('Archivos eliminados')    
   

#Hecho por Zodiako :)